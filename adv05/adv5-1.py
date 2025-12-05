from aocd import get_data
data = get_data(year=2025, day=5)
ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in data.split("\n\n")[0].split("\n")]
ids = [int(x) for x in data.split("\n\n")[1].split("\n")]
ans = 0

for id in ids:
    
    for range in ranges:
        
        if (range[0] <= id and id <= range[1]):
            ans += 1
            break
        
print(ans)
