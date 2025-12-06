from aocd import get_data
from math import prod
data = get_data(year=2025, day=6).split("\n")
inputs = []

for line in data:
    inputs.append(line)
ans = 0
string = ""

for i in range(len(inputs[0])-1,-1,-1):
    s = ""
    for j in range(len(inputs)):
        s += inputs[j][i]
    string += s
    
parsed = string.split()
answers = []
to_add = []

for input in parsed:
    
    if (input[-1] == "+"):
        
        if (len(input)>1):
            to_add.append(int(input[:-1]))
        answers.append(sum(to_add))
        to_add = []
        
    elif (input[-1] == "*"):
        
        if (len(input) > 1):
            to_add.append(int(input[:-1]))
        answers.append(prod(to_add))
        to_add = []
        
    else:
        to_add.append(int(input))
        
print(sum(answers))