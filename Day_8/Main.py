import numpy as np
from collections import Counter


def get_input(name = '', test = False):
    if not name:
        if test:
            name =  r'/'.join(__file__.split(r'/')[-3:-1]) + r'/test_input.txt'
        else:
            name =  r'/'.join(__file__.split(r'/')[-3:-1]) + r'/input.txt'

    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line)
        
        if len(lines) == 1:
            lines = lines[0]
    if test:
        width = 2; height = 2
    else:
        width = 25; height = 6

    part2 = np.array([int(each) for each in lines])
    part2 = np.reshape(part2, (-1, height, width))
    return part2



if __name__ == "__main__":
    import time
    t0 = time.time()
    part1 = 0

    inp = get_input()

    layers,height,width = inp.shape
    best = 0
    best_l = None
    for l in range(layers):
        nonz = np.count_nonzero(inp[l,:,:])

        if nonz > best:
            best = nonz
            best_l = l

    unique, counts = np.unique(inp[best_l,:,:], return_counts=True)
    part1 = dict(zip(unique, counts))
    t1 = time.time()

    """ -------------------------------------------------------------------------------- """

    part2 = None

    inp = get_input()
    layers,height,width = inp.shape

    part2 = []

    for y in range(height):
        part2.append("")
        for x in range(width):
            l = np.where( inp[:,y,x] != 2)[0][0]
            if inp[l,y,x]:
                part2[y] += '#'
            else:
                part2[y] += ' '

    np.set_printoptions(linewidth= 100)
    for each in part2:
        print(each)
    print()

    t2 = time.time()






    print(f"Part 1 -- {part1[1] * part1[2]}, t: {t1-t0:0.4f}")
    print(f"Part 2 -- {part2}, t: {t2-t1:0.4f}")
    print(f"total time = {t2-t0:0.4f}")