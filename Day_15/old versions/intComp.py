import time
import math

def get_input(name = '', test = False):
    if not name:
        if test:
            name =  r'/'.join(__file__.split(r'/')[-3:-1]) + r'/test_input.txt'
        else:
            name =  r'/'.join(__file__.split(r'/')[-3:-1]) + r'/input.txt'

    with open(name) as f:
        lines = []
        for line in f:
            lines.append( list(map(int, line.split(','))))
        if len(lines) == 1:
            lines = lines[0]

        return lines


class opComp():
    def __init__(self, memory, inp = None, outlen = 0):
        self.outlen = outlen
        self.input_l = []
        if inp != None:
            self.input_l.append(inp)
        self.memory = memory[:]
        self.memSize = len(self.memory)
        memory = None


        self.opcodes = {
            "01" : self.opCode1,
            "02" : self.opCode2,
            "03" : self.opCode3,
            "04" : self.opCode4,
            "05" : self.opCode5,
            "06" : self.opCode6,
            "07" : self.opCode7,
            "08" : self.opCode8,
            "09" : self.opCode9,
            "99" : self.opCode99
        }

        self.instPoint = 0
        self.inputPoint = 0
        self.relBase = 0

        self.output = []
        self.finished = False
        self.opcodes_run = 0


        if inp != None:
            self.run_prog()

    def set_memory(self, ind, inp):
        self.memory[ind] = inp

    def run_prog(self, inp = None, ret = False):
        if self.finished:
            print('this program is done, but tried to run again')
            return 'this program is done, but tried to run again'
        if inp != None:
            self.input_l.append(inp)
        self.running = True
        while self.instPoint < self.memSize and self.running and not self.finished:
            instruction = [each for each in str(self.memory[self.instPoint])]
            mod3,mod2,mod1, *ins = (5-len(instruction)) * ['0'] + instruction; ins = ''.join(ins)
            if ins in self.opcodes:
                self.opcodes[ins](list(map(int, [mod1,mod2,mod3])))
                self.opcodes_run += 1
            else:
                print(mod1, mod2, mod3, ins)
                break
        self.last_op = ins
        if ret:
            return self.output[-self.outlen]


    def instructions(self):
        outlen = self.outlen
        ins = []
        for i in range(0,len(self.output), outlen):
            ins.append(self.output[i:i+outlen])
        return ins


    # -----------------------------------------------------------------------------------------------------------------------
    def opCode1(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(modes[2], self.instPoint+3, param1 + param2)
        self.instPoint += 4
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode2(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(modes[2], self.instPoint+3, param1 * param2)
        self.instPoint += 4
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode3(self, modes = None):
        if self.inputPoint >= len(self.input_l):
            self.running = False
            return
        inp = self.input_l[self.inputPoint]; self.inputPoint += 1
        self.set_param(modes[0], self.instPoint+1, inp)
        self.instPoint += 2
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode4(self, modes = None):

        out = self.get_param(modes[0], self.instPoint+1)
        self.output.append(out)
        self.instPoint += 2
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode5(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        if param1 != 0:
            self.instPoint = param2
            return
        self.instPoint += 3
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode6(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        if param1 == 0:
            self.instPoint = param2
            return
        self.instPoint += 3
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode7(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(modes[2], self.instPoint+3, int(param1 < param2))
        self.instPoint += 4
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode8(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        param2 = self.get_param(modes[1], self.instPoint+2)
        self.set_param(modes[2], self.instPoint+3, int(param1 == param2))
        self.instPoint += 4
    # -----------------------------------------------------------------------------------------------------------------------
    def opCode9(self, modes = None):
        param1 = self.get_param(modes[0], self.instPoint+1)
        self.relBase += param1
        self.instPoint += 2
        


    def opCode99(self, modes = None):
        self.running = False
        self.instPoint += 1
        self.finished = True

    def get_index(self, mode, index):
        if   mode == 0:
            index = self.memory[index]
        elif mode == 1:
            index = index
        elif mode == 2:
            index = self.relBase + self.memory[index]
        else:
            print('Wrong mode encountered')
        if index >= self.memSize:
            newMem = (index - self.memSize) + 1
            self.memory += newMem * [0]
            self.memSize += newMem
        return index

    def get_param(self, mode, index):
        return self.memory[self.get_index(mode,index)]
    
    def set_param(self, mode, index, value):
        # print(self.get_index(mode, index), ' -:- ', self.memory[index])
        self.memory[self.get_index(mode,index)] = value



if __name__ == "__main__":
    import Main_v1