from qunetsim import Qubit, Network
import networkx as nx
import random

def bell_measurement(sender, receiver):
    q1, q2 = Qubit.entangled_pair(sender)
    sender.send_teleport(q1, receiver)
    return q2

def djikstra_routing(network, source, destination):
    # Use Dijkstra's algorithm to find the shortest path from source to destination
    shortest_path = nx.shortest_path(network.topology, source, destination)
    return shortest_path

def quantum_routing(network, source, destination, qubit):
    # Find shortest path using Dijkstra's algorithm
    shortest_path = djikstra_routing(network, source, destination)

    # Route qubit along the shortest path
    current_node = source
    for i in range(len(shortest_path) - 1):
        next_node = shortest_path[i + 1]
        qubit = bell_measurement(current_node, next_node)
        current_node = next_node
    
    return qubit

# Initialize the quantum network
network = Network.get_instance()
network.start()

# Add nodes to the network
network.add_node('Node1')
network.add_node('Node2')
network.add_node('Node3')
network.add_node('Node4')

# Add links to the network
network.add_link('Node1', 'Node2')
network.add_link('Node1', 'Node3')
network.add_link('Node2', 'Node4')
network.add_link('Node3', 'Node4')

# Define source and destination nodes
source_node = 'Node1'
destination_node = 'Node4'

# Create a qubit at the source node
qubit = Qubit(network.get_node(source_node))

# Perform quantum routing
routed_qubit = quantum_routing(network, source_node, destination_node, qubit)
print(f"Qubit routed from {source_node} to {destination_node}")

# Stop the network simulation
network.stop()
