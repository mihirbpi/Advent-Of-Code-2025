from aocd import get_data
data = get_data(year=2025, day=2).split(",")

def get_invalid_ids(start, end):
    ids = set()
    
    for n in range(start, end+1):
        s = str(n)
        
        for l in range(1,len(s)):
            found = False
            
            for k in range(2,len(s)+1):
                
                if (s == k*s[:l]):
                    ids.add(n)
                    found = True
                    break
                
            if (found):
                break
    return list(ids)
        

ans = 0

for data_string in data:
    invalid_ids = get_invalid_ids(*[int(x) for x in data_string.split("-")])
    ans += sum(invalid_ids)
        
print(ans)   