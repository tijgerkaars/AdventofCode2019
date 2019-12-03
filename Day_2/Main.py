import time
import math

class opComp():
    def __init__(self, memory, validate = None, initialize = None):
        self.memory = memory[:]
        memory = None

        if initialize:
            for each in initialize:
                i, value = each
                self.memory[i] = value

        self.opcodes = {
            1  : self.opCode1,
            2  : self.opCode2,
            99 : self.opCode99
        }

        self.memSize = len(self.memory)
        self.instPoint = 0
        self.running = True
        while self.instPoint < self.memSize and self.running:
            instruction = self.memory[self.instPoint]
            self.opcodes[instruction]()
        self.output = self.memory[0]


    def opCode1(self):
        parameter_1 = memory[self.instPoint+1]; parameter_2 = memory[self.instPoint+2]; parameter_3 = memory[self.instPoint+3]
        self.memory[parameter_3] = self.memory[parameter_1] + self.memory[parameter_2]
        self.instPoint += 4
    def opCode2(self):
        parameter_1 = memory[self.instPoint+1]; parameter_2 = memory[self.instPoint+2]; parameter_3 = memory[self.instPoint+3]
        self.memory[parameter_3] = self.memory[parameter_1] * self.memory[parameter_2]
        self.instPoint += 4
    def opCode99(self):
        self.running = False
        self.instPoint += 1


if __name__ == "__main__":
    t1 = time.time()
    memory = [1,0,0,0,99]
    print(memory)
    c1 = opComp(memory, validate=[2,0,0,0,99])
    print(c1.memory, end='\n\n')

    memory = [2,3,0,3,99]
    print(memory)
    c2 = opComp(memory, validate=[2,3,0,6,99])
    print(c2.memory, end='\n\n')

    memory = [2,4,4,5,99,0]
    print(memory)
    c3 = opComp(memory, validate=[2,4,4,5,99,9801])
    print(c3.memory, end='\n\n')

    memory = [1,1,1,4,99,5,6,0,99]
    print(memory)
    c4 = opComp(memory, validate=[30,1,1,4,2,5,6,0,99])
    print(c4.memory, end='\n\n')

    lines = []
    with open(r'AdventofCode2019\Day_1\Input.txt') as file:
        for line in file:
            lines.append( list(map( int, line.strip().split(',') ) ) )
        if len(lines) == 1:
            lines = lines[0]
        memory = lines
    c = opComp(memory, initialize=([(1,12),(2,2)]))
    print(f"Part 1 -- {c.output}", '\n')

    for noun in range(100):
        for verb in range(100):
            c = opComp(memory, initialize=([(1,noun),(2,verb)]))
            if c.output == 19690720:
                print(f"Part 2 -- Noun: {noun}, Verb: {verb}, ans = {100*noun + verb}")

    print(f"Total time: {time.time() - t1}")