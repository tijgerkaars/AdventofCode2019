import math

lines = []
with open(r'AdventofCode2019\Day_1\Input.txt') as file:
    for line in file:
        lines.append( list(map( int, line.strip().split(',') ) ) )
    if len(lines) == 1:
        lines = lines[0]
    memory = lines  

""" 
# setup for repair
memory[1] = 12; memory[2] = 2

l = len(memory)

for i in range(0,l,4):
    instruction = memory[i]
    if instruction == 99:
        break
    
    parameter_1 = memory[i+1]; parameter_2 = memory[i+2]; parameter_3 = memory[i+3]

    if instruction == 1:
        memory[parameter_3] = memory[parameter_1] + memory[parameter_2]
    elif instruction == 2:
        memory[parameter_3] = memory[parameter_1] * memory[parameter_2]
 """


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
    memory = [1,0,0,0,99]
    c1 = opComp(memory, validate=[2,0,0,0,99])
    memory = [2,3,0,3,99]
    c2 = opComp(memory, validate=[2,3,0,6,99])
    memory = [2,4,4,5,99,0]
    c3 = opComp(memory, validate=[2,4,4,5,99,9801])
    memory = [1,1,1,4,99,5,6,0,99]
    c4 = opComp(memory, validate=[30,1,1,4,2,5,6,0,99])

    lines = []
    with open(r'AdventofCode2019\Day_1\Input.txt') as file:
        for line in file:
            lines.append( list(map( int, line.strip().split(',') ) ) )
        if len(lines) == 1:
            lines = lines[0]
        memory = lines
    print(memory)
    c = opComp(memory, initialize=([(1,12),(2,2)]))
    print(memory)
    for noun in range(100):
        for verb in range(100):
            c = opComp(memory, initialize=([(1,noun),(2,verb)]))
            if c.output == 19690720:
                print(f"Noun: {noun}, Verb: {verb}, ans = {100*noun + verb}")
