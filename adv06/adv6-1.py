from aocd import get_data
data = get_data(year=2025, day=6).split("\n")
ops = []
inputs = []

for line in data:
    line_split = line.split(" ")
    input = []
    
    for x in line_split:
        if x != '':
            input.append(x)
            
    if ('*' in input or '+' in input):
        ops = input
    else:
        inputs.append(input)
ans = 0
for i in range(len(ops)):
    op = ops[i]
    
    if (op == '+'):
        sub_ans = 0
        
        for j in range(len(inputs)):
            sub_ans += int(inputs[j][i])
    else:
        sub_ans = 1
        
        for j in range(len(inputs)):
            sub_ans *= int(inputs[j][i])
    ans += sub_ans
    
print(ans)