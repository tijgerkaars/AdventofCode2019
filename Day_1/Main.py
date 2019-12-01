import math

lines = []
with open(r'AdventofCode2019\Day_1\Input.txt') as file:
    for line in file:
        lines.append( math.floor( int(line.strip()) / 3 ) - 2 )
    
print(f"part 1: {sum(lines)}")

all_fuel = []
for each in lines:
    t = 0
    while each  > 0:
        t += each
        each  = math.floor(each/3) - 2
    all_fuel.append(t)
print(f"part 2: {sum(all_fuel)}")
