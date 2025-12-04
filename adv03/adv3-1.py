from aocd import get_data
data = get_data(year=2025, day=3).split("\n")

ans = 0

for bank in data:
    max_joltage = -1e99
    
    for i in range(len(bank)-1):
        
        for j in range(i+1,len(bank)):
            max_joltage = max(max_joltage, int(bank[i]+bank[j]))
            
    ans += max_joltage
    
print(ans)