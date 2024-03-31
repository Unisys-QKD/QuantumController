from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

class CustomTopology(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add switches and hosts
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1')

        # Add links
        self.addLink(h1, s1)

        
        h2 = self.addHost('h2')

        # Add links
        self.addLink(h2, s1)

def run_custom_topology():
    topo = CustomTopology()
    net = Mininet(topo=topo, controller=RemoteController)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run_custom_topology()