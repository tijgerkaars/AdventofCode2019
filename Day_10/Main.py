import math
from math import pi
from queue import PriorityQueue

test = 'test'

def get_input(test = False):
    if test:
        name = r'AdventofCode2019\Day_10\test_input.txt'
    else:
        name = r'AdventofCode2019\Day_10\input.txt'
    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line.strip())
        if len(lines) == 1:
            lines = lines[0]
        return lines

def format_input(inp):
    plus = 0
    new_inp = dict()
    for y,row in enumerate(inp):
        print(row)
        for x, square in enumerate(row):
            if square != '.':
                plus += 1
                new_inp[(x,y)] = dict()
    print(f'\n{plus} Asteroids on map')
    print('#----------------------------------------------------------------------------------')
    return new_inp


def find_observable(asteroid, others, test = False):
    if test:
        x,y = [0,0]
        s = (x,y)
        other = (x,y-1); print( find_angle(s,other) ) # up
        other = (x-1,y); print( find_angle(s,other) ) # left
        other = (x,y+1); print( find_angle(s,other) ) # down
        other = (x+1,y); print( find_angle(s,other) ) # right
    angles = dict()
    for each in others:
        if each != asteroid:
            angle = find_angle(asteroid,each)
            if angle not in angles:
                angles[angle] = []
            angles[angle].append(each)
    for angle, obj in angles.items():
        angles[angle] = order_list(asteroid, obj)
    return angles

def order_list(point, l):
    n = l[:]
    n.sort(key = lambda p: dist(point, p))
    return n

def dist(p1, p2):
    x1,y1 = p1; x2,y2 = p2
    return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

def deg_atan2(dy, dx):
    return math.degrees( math.atan2( dy, dx) ) % 360

def find_angle(asteroid, other):
    x1,y1 = asteroid; x2,y2 = other
    return deg_atan2(
        (y2-y1), (x2-x1)
    )

def find_best_spot(data):
    best = 0; top_spot = None
    for key, _ in data.items():
        if len(data[key]) > best:
            best = len(data[key])
            top_spot = key
    return top_spot, best

def next_angle(prev, angles):
    if prev >= angles[-1]:
        return angles[0]
    for each in angles:
        if each > prev:
            return each
    pass

def fire_laser(data,angle = 270):
    angles = list(data.keys()); angles.sort()
    if angle not in angles:
        angle = next_angle(angle, angles)
    astroid = data[angle][0]
    data[angle].remove(astroid)
    if len(data[angle]) == 0:
        data.pop(angle, None)
    angle = next_angle(angle, angles)
    return astroid, angle

    

    # print(point, angles)
    # print(data[angles[0]])
    
    # x,y = point
    # other = (x,y-1); print( find_angle(point,other) ) # up



def mark_order(spots, inp):
    l = inp[:]
    for i, spot in enumerate(spots):
        x,y = spot
        fill = str(i)
        if i == 0:
            fill = "X"
        l[y] = l[y][:x] + fill + l[y][x+1:]
    [print(each) for each in l]

def pprint(spot, inp):
    l = inp[:]
    x,y = spot
    l[y] = l[y][:x] + 'X' + l[y][x+1:]    
    [print(each) for each in l]


if __name__ == "__main__":
    import time
    t0 = time.time()
    
    inp = get_input(test=False)
    data = format_input(inp)
    for asteroid in data:
        l = find_observable(asteroid,list(data.keys()))
        data[asteroid] = l
    bestSpot, sees = find_best_spot(data)
    print(bestSpot, sees)
    part1 = sees; t1 = time.time()
    
    order = []
    angle = 270
    for _ in range(299):
        ast, angle = fire_laser(data[bestSpot], angle)
        order.append(ast)
    order = [bestSpot] + order
    x,y = order[200]; part2 = x*100+y
    print(order[200])
    t2 = time.time()

    print(f"Part 1 -- {part1}, t: {t1-t0:0.4f}")
    print(f"Part 2 -- {part2}, t: {t2-t1:0.4f}")
    print(f"total  -- t: {t2-t0:0.4f}")

    
