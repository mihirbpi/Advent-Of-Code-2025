from aocd import get_data
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
            
            
def get_num_splits(start_pos, splits):
    curr_pos = start_pos
    reached_end = False
    
    while(not reached_end):
        curr_row, curr_col = curr_pos
        if (grid[curr_pos] == '^'):
            
            if (curr_pos not in splits):
                splits.append(curr_pos)
                
                if ((curr_row,curr_col-1) not in splits):
                    get_num_splits((curr_row,curr_col-1), splits)
                if ((curr_row,curr_col+1) not in splits):
                    get_num_splits((curr_row,curr_col+1), splits)
            reached_end = True
            
        if (not reached_end):
            curr_row += 1
            curr_pos = (curr_row, curr_col)
            reached_end = (curr_row >= len(data)-1)
        
splits = []
get_num_splits(start, splits)
print(len(splits))
        
    
    