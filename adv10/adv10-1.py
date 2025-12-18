from aocd import get_data
from itertools import product
import heapq
data = get_data(year=2025, day=10).split("\n")

def toggle(press, lights):
    s = list(lights)
    for idx in press:
        if(lights[idx] == "#"):
            s[idx] = "."
        elif(lights[idx] == "."):
            s[idx] = "#"
    return "".join(s)

def dijkstra(neighbors, src, dist):

    pq = []
    heapq.heapify(pq)
    dist[src] = 0
    heapq.heappush(pq, (0, src))
    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in neighbors[u]:
            
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

ans = 0
    
for line in data:
    spl = line.split(" ")
    lights = spl[0][1:-1]
    presses = [list(map(int, x[1:-1].split(","))) for x in spl[1:-1]]
    joltages = list(map(int,spl[-1][1:-1].split(",")))
    dist = {}
    neighbors = {}
    src = "."*len(lights)
    
    for binary_tuple in product('.#', repeat=len(lights)):
        light_seq = "".join(binary_tuple)
        dist[light_seq] = 1e99
        reacheable = [(toggle(press, light_seq), 1) for press in presses]
        
        if (light_seq not in neighbors):
            neighbors[light_seq] = set(reacheable)
        else:
            neighbors[light_seq].update(reacheable)
            
    final_dist = dijkstra(neighbors.copy(),src,dist.copy())
    ans += final_dist[lights]
print(ans)