from aocd import get_data
data = get_data(year=2025, day=3).split("\n")

def find_max_num_formed(seq,n):
    if n == 1:
        return max([int(x) for x in seq[:len(seq)-n+1]])
    max_now = max([int(x) for x in seq[:len(seq)-n+1]])
    indices = []
    
    for i in range(len(seq)):
        
        if int(seq[i]) == max_now and i < len(seq)-n+1:
            indices.append(i)
    result = -1e99
    
    for index in indices:
        new_seq = seq[index+1:]
        result = max(result,int(str(max_now) + str(find_max_num_formed(new_seq,n-1))))
        
    return result
    
ans = 0

for bank in enumerate(data):
    ans += find_max_num_formed(bank,12)
    
print(ans)