from aocd import get_data
data = get_data(year=2025, day=1).split("\n")
dial = 50
count = 0

for instruction in data:
    dir, amount = instruction[0], int(instruction[1:])
    dir = 1 if dir == "R" else -1
    dial = (dial + dir*amount) % 100
    
    if (dial == 0):
        count += 1
print(count)