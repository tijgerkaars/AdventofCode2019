import time
import math

if __name__ == "__main__":
    t1 = time.time()


    lines = []
    with open(r'AdventofCode2019\Day_3\Input.txt') as file:
        for line in file:
            lines.append( line )

    directions = {
        'U' : ( 0, 1),
        'D' : ( 0,-1),
        'L' : (-1, 0),
        'R' : ( 1, 0)
    }
    
    wires = []  # part 1
    wires_length = [] # part 2
    for wire in lines:
        coord = (0,0)
        new_wire = set()
        new_wire_length = []
        wire = wire.split(",")
        for stretch in wire:
            d, *s = stretch; s = int("".join(s))
            dx, dy = directions[d]
            for i in range(s):
                x,y = coord
                coord = (x+dx, y+dy)
                new_wire.add(coord)
                new_wire_length.append(coord)
        wires.append(new_wire)
        wires_length.append(new_wire_length)
    
    junctions = wires[0].intersection(wires[1])
    dist = [abs(each[0]) + abs(each[1]) for each in junctions]
    

    junc_dist = dict.fromkeys(junctions, 0)

    for wire in wires_length:
        found = set()
        for i, step in enumerate(wire):
            if step in junc_dist and step not in found:
                found.add(step)
                junc_dist[step] += (i+1)
    
    print(f"\nPart 1 -- {min(dist)}")
    print(f"Part 2 -- {min(junc_dist.values())}")

    
    















    print(f"\nTotal time: {time.time() - t1}")