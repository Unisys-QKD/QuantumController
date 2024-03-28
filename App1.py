import tornado.ioloop
import tornado.web
from ryu.base import app_manager
from ryu.controller.controller import Datapath
from ryu.lib import hub
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from webob import Response
from mininet.log import setLogLevel  
from ryu.lib.packet import packet, ethernet
from ryu.lib.packet.ethernet import ether


import json

class CustomRyuApp(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, topo=None, *args, **kwargs):
        super(CustomRyuApp, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.topology = topo

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, MAIN_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Install table-miss flow entry
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)

        if eth.ethertype == ether.ETH_TYPE_LLDP:
            return  # Ignore LLDP packets

        dst = eth.dst
        src = eth.src

        self.mac_to_port.setdefault(datapath.id, {})
        self.mac_to_port[datapath.id][src] = in_port

        if dst in self.mac_to_port[datapath.id]:
            out_port = self.mac_to_port[datapath.id][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)

        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions, data=data)
        datapath.send_msg(out)

class NetworkTopologyHandler(tornado.web.RequestHandler):
    def initialize(self, ryu_app):
        self.ryu_app = ryu_app

    def get(self):
        topology = self.ryu_app.topology.to_dict()
        self.write(json.dumps(topology))


class MininetRyuTornadoApp:
    def __init__(self, topo=None):
        self.topo = topo
        self.ryu_app = CustomRyuApp(topo=topo)
        self.application = tornado.web.Application([
            (r"/custom/topology", NetworkTopologyHandler, dict(ryu_app=self.ryu_app)),
        ])

    def start(self):
        self.ryu_app.start()
        self.application.listen(8888)
        tornado.ioloop.IOLoop.current().start()

    def stop(self):
        self.ryu_app.stop()
        tornado.ioloop.IOLoop.current().stop()

if __name__ == "__main__":
    from mininet_setup import CustomTopology, start_mininet
    setLogLevel('info')
    topo = CustomTopology()
    start_mininet(topo)
    app = MininetRyuTornadoApp(topo=topo)
    app.start()
