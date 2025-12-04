from aocd import get_data
from collections import defaultdict
data = get_data(year=2025, day=4).split("\n")
grid_dict = defaultdict(lambda: "")

for row in range(len(data)):
    
    for col in range(len(data[0])):
        grid_dict[(row,col)] = data[row][col]
        
ans = 0

for row in range(len(data)):
    
    for col in range(len(data[0])):
        
        if (grid_dict[(row,col)] == "@"):
            dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
            count = 0
            
            for dir in dirs:
                
                if(grid_dict[(row+dir[0],col+dir[1])] == "@"):
                    count += 1
                    
            if (count < 4):
                ans += 1

print(ans)       