from aocd import get_data
import networkx as nx
import math
data = [tuple(map(int, x.split(","))) for x in get_data(year=2025, day=8).split("\n")]
G = nx.Graph()
G.add_nodes_from(data)
num_circuits = float("inf")

def dist(n1, n2):
    return math.sqrt(sum([(n1[i]-n2[i])**2 for i in range(3)]))

node_pairs = set()
for node1 in data:
    
    for node2 in data:
        
        if (node1 != node2):
            node_pairs.add(tuple(sorted((node1,node2))))

node_pairs = sorted(list(node_pairs), key=lambda x: dist(x[1],x[0]))
while (num_circuits > 1):
    closest = (node_pairs[0][0], node_pairs[0][1])
    
    if ((closest[0], closest[1]) in node_pairs or (closest[1], closest[0]) in node_pairs):
        G.add_edge(closest[0], closest[1])
        G.add_edge(closest[1], closest[0])
    node_pairs = node_pairs[1:]
    num_circuits = len(list(nx.connected_components(G)))
    
    if(num_circuits == 1):
        print(closest[0][0]*closest[1][0])     