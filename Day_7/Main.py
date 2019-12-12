from intComp   import opComp
from itertools import permutations


def sequencer(l):
    return list( permutations(l, len(l)))

def get_input(test = False):
    if test:
        fn = r"AdventofCode2019\Day_7\test_input.txt"
    else:
        fn = r"AdventofCode2019\Day_7\input.txt"
    with open(fn) as f:
        lines = []
        for line in f:
            lines.append( list(map(int, line.strip().split(','))))
        if len(lines) == 1:
            lines = lines[0]

        return lines


import time
t0 = time.time()
program = get_input()


seq = sequencer([i for i in range(5,10)])

part2 = 0

for A,B,C,D,E in seq:
    counter = 0
    cA = opComp(program, inp=A)
    cB = opComp(program, inp=B)
    cC = opComp(program, inp=C)
    cD = opComp(program, inp=D)
    cE = opComp(program, inp=E)

    done = sum([int(each.finished) for each in [cA, cB, cC, cD, cE]])
    print(done)

    Ain = 0
    counter = 0; limit = 1000

    while not done and counter < limit:
        Bin = cA.run_prog(Ain)
        Cin = cB.run_prog(Bin)
        Din = cC.run_prog(Cin)
        Ein = cD.run_prog(Din)
        Ain = cE.run_prog(Ein)
        done = sum([int(each.finished) for each in [cA, cB, cC, cD, cE]])
        
        counter += 1
    part2 = max(part2, cE.output)

if counter == limit-1:
    print(f'bad exit -- counter: {counter}')
else:
    print(f'good exit -- {part2}')

