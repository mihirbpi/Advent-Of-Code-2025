from aocd import get_data
from collections import defaultdict
data = get_data(year=2025, day=4).split("\n")
grid_dict = defaultdict(lambda: "")

for row in range(len(data)):
    
    for col in range(len(data[0])):
        grid_dict[(row,col)] = data[row][col]

def get_rolls_accessible(data,grid_dict):      
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
                    grid_dict[(row,col)] = "."
                    ans += 1
    return ans

rolls_accessible = get_rolls_accessible(data,grid_dict)
ans = rolls_accessible

while(rolls_accessible > 0):
    rolls_accessible = get_rolls_accessible(data,grid_dict)
    ans += rolls_accessible

print(ans)