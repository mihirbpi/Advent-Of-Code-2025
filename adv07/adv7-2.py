from aocd import get_data
from functools import cache
from collections import defaultdict
data = get_data(year=2025, day=7).split("\n")

grid = defaultdict(lambda: 0)

for row in range(len(data)):
    
    for col in range(len(data[0])):
        
        if (data[row][col] == 'S'):
            start = (row, col)
            grid[(row,col)] = '.'
        else:
            grid[(row,col)] = data[row][col]
path_count = 0          

@cache
def get_num_paths(start_pos):
    row, col = start_pos
    
    if ((row >= len(data)-1)):
        return 1
    if (grid[start_pos] == '^'):
        return get_num_paths((row,col-1))+get_num_paths((row,col+1))
    else:
        return get_num_paths((row+1,col))
        
visited = set()
print(get_num_paths(start))