import time
import math

def get_input():
    with open(r"AdventofCode2019\Day_5\input.txt") as f:
        lines = []
        for line in f:
            lines.append( list(map(int, line.split(','))))
        if len(lines) == 1:
            lines = lines[0]

        return lines


class opComp():
    def __init__(self, memory, validate = None, initialize = None, inp = None):
        self.test_input = inp
        self.memory = memory[:]
        memory = None

        if initialize:
            for each in initialize:
                i, value = each
                self.memory[i] = value

        self.opcodes = {
            "01" : self.opCode1,
            "02" : self.opCode2,
            "03" : self.opCode3,
            "04" : self.opCode4,
            "05" : self.opCode5,
            "06" : self.opCode6,
            "07" : self.opCode7,
            "08" : self.opCode8,
            "99" : self.opCode99
        }

        tests = 0
        self.memSize = len(self.memory)
        self.instPoint = 0
        self.running = True
        while self.instPoint < self.memSize and self.running:
            instruction = [each for each in str(self.memory[self.instPoint])]
            mod3,mod2,mod1, *ins = (5-len(instruction)) * ['0'] + instruction; ins = ''.join(ins)
            if ins == '04' and False:
                if tests > 0:
                    print(self.memory[self.instPoint:])
                    break
                tests += 1
            if ins in self.opcodes:
                self.opcodes[ins](list(map(int, [mod1,mod2,mod3])))
            else:
                print(mod1, mod2, mod3, ins)
                break


    def opCode1(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(self.instPoint+3, param1 + param2)
        self.instPoint += 4
    def opCode2(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(self.instPoint+3, param1 * param2)
        self.instPoint += 4
    def opCode3(self, modes = None):
        inp = self.test_input
        self.set_param(self.instPoint+1, inp)
        self.instPoint += 2
    def opCode4(self, modes = None):
        print(self.memory[self.memory[self.instPoint+1]])
        self.instPoint += 2
    def opCode5(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        if param1 != 0:
            self.instPoint = param2
            return
        self.instPoint += 3
    def opCode6(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        if param1 == 0:
            self.instPoint = param2
            return
        self.instPoint += 3
    def opCode7(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(self.instPoint+3, int(param1 < param2))
        self.instPoint += 4
    def opCode8(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(self.instPoint+3, int(param1 == param2))
        self.instPoint += 4
        


    def opCode99(self, modes = None):
        self.running = False
        self.instPoint += 1

    def get_param(self, mode, index):
        if mode == 0:
            return self.memory[self.memory[index]]
        elif mode == 1:
            return self.memory[index]
        else:
            print('Wrong mode encountered')
    
    def set_param(self, index, value):
        self.memory[self.memory[index]] = value



if __name__ == "__main__":
    t0 = time.time()
    
    raw = []
    if not raw:
        raw = get_input()
    i = 5
    print(f"input: {i} -- ", end= "")
    c = opComp(raw, inp=i)

    print(f"Total time: {time.time() - t0}")

    # not 223