from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.log import setLogLevel
from mininet.node import Host


class CustomTopology(Topo):
    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')

        self.addLink(h1, s1)
        self.addLink(h2, s1)

    def to_dict(self):
        # Convert the topology into a dictionary
        topology_dict = {
            'hosts': [host.name for host in self.nodes() if isinstance(host, Host)],
            'switches': [switch for switch in self.switches()],
            'links': [(self.link_info(link)) for link in self.links()]
        }
        return topology_dict

    def link_info(self, link):
        # Ensure link is a tuple of two nodes
        if isinstance(link, tuple) and len(link) == 2:
            return (link[0], link[1])
        else:
            return None




def start_mininet(topo):  
    net = Mininet(topo=topo, switch=OVSSwitch, controller=RemoteController, autoSetMacs=True)
    net.start()
    net.pingAll()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h1.setIP('192.168.0.1/24')
    h2.setIP('192.168.0.2/24')
    h1.cmd('ip route add default via 192.168.0.2')
    h2.cmd('ip route add default via 192.168.0.1')

    net.stop()

if __name__ == "__main__":
    setLogLevel('info')
    start_mininet()
