from aocd import get_data
data = get_data(year=2025, day=9).split("\n")
data = [tuple(map(int, x.split(","), )) for x in data]

def rect_area(p1,p2):
    return (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)

max_area = float("-inf")
for p1 in data:
    
    for p2 in data:
        
        if (p1 != p2):
            area = rect_area(p1,p2)
            max_area = max(max_area, area)
            
print(max_area)