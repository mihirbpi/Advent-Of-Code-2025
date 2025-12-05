from aocd import get_data
data = get_data(year=2025, day=5)
ranges = [[int(x.split("-")[0]), int(x.split("-")[1])] for x in data.split("\n\n")[0].split("\n")]
ranges = sorted(ranges, key=lambda x: x[0])
new_ranges = []
new_ranges.append(ranges[0])

for i in range(1, len(ranges)):
    last = new_ranges[-1]
    curr = ranges[i]
    
    if (curr[0] <= last[1]):
        last[1] = max(last[1], curr[1])
    else:
        new_ranges.append(curr)
        
ans = 0

for range in new_ranges:
    ans += range[1] - range[0] + 1
    
print(ans)
