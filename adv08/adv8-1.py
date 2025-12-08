from aocd import get_data
import networkx as nx
import math
data = [tuple(map(int, x.split(","))) for x in get_data(year=2025, day=8).split("\n")]
G = nx.Graph()
G.add_nodes_from(data)
n_iters = 1000

def dist(n1, n2):
    return math.sqrt(sum([(n1[i]-n2[i])**2 for i in range(3)]))

node_pairs = set()
for node1 in data:
    
    for node2 in data:
        
        if (node1 != node2):
            node_pairs.add(tuple(sorted((node1,node2))))

node_pairs = sorted(list(node_pairs), key=lambda x: dist(x[1],x[0]))

for iter in range(n_iters):
    closest = (node_pairs[0][0], node_pairs[0][1])
    
    if ((closest[0], closest[1]) in node_pairs or (closest[1], closest[0]) in node_pairs):
        G.add_edge(closest[0], closest[1])
        G.add_edge(closest[1], closest[0])
    node_pairs = node_pairs[1:]

ans = math.prod(sorted([len(c) for c in nx.connected_components(G)], reverse=True)[:3])
print(ans)      