import time
import math
from intComp import opComp

def get_input(name = '', test = False):
    if not name:
        if test:
            name =  r'/'.join(__file__.split(r'/')[-3:-1]) + r'/test_input.txt'
        else:
            name =  r'/'.join(__file__.split(r'/')[-3:-1]) + r'/input.txt'
    if name != '':
        with open(name) as f:
            lines = []
            for line in f:
                lines.append( list(map(int, line.split(','))))
            if len(lines) == 1:
                lines = lines[0]

            return lines

def test():
    program = get_input(test=True)
    for each in program:
        c1 = opComp(each, inp=2)
        print( f"codes ran: { c1.opcodes_run}, l: {len(str(c1.output))} out: {c1.output}")

if __name__ == "__main__" or True:
    t0 = time.time()
    """ ------------------------------------------------------------------------------------------------------------------ """
    debug = False

    if debug:
        test()
        part1 = None
    else:
        program = get_input()
        c1 = opComp(program, inp=1)
        print( f"codes ran: { c1.opcodes_run}, l: {len(str(c1.output))} out: {c1.output}")
        part1 = c1.output[0]
    
    t1 = time.time()
    """ ------------------------------------------------------------------------------------------------------------------ """
    
    program = get_input()
    c1 = opComp(program, inp=2)
    print( f"codes ran: { c1.opcodes_run}, l: {len(str(c1.output))} out: {c1.output}")
    part2 = c1.output[0]
    
    
    t2 = time.time()

    print(f"Part 1 -- {part1}, t: {t1-t0:0.4f}")
    print(f"Part 2 -- {part2}, t: {t2-t1:0.4f}")
    print(f"total, t: {t2-t0:0.4f}")