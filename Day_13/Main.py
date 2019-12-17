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

class Robot():
    def __init__(self, inp = None, outlen = 1):
        memory = get_input()
        self.memory = memory[:]
        self.comp = opComp(memory[:], outlen=outlen)
        self.outlen = outlen

        self.tile_ids = {
            0 : ' ',
            1 : '|',
            2 : '#',
            3 : '~',
            4 : 'O'     }
        self.inp_map = {
            'a': -1,
            's':  0,
            'd':  1    }
        
        
        
        self.comp.run_prog(inp)
        if self.comp.opcodes_run == 0:
            print(f'No code was executed, finished: {self.comp.finished}')
        inst = self.comp.instructions()
        self.test = inst
        rx, ry = self.game_dims(inst)

        game = []
        for y in ry:
            game.append([])
            for _ in rx:
                game[y].append([])
        self.ball = None     
        self.paddle = None           
        self.blocks = set()
        for i in inst:
            x,y,id = i
            game[y][x] = id
            if id == 2:
                self.blocks.add((x,y))
            elif id == 4:
                self.ball = (x,y)
            elif id == 3:
                self.paddle = (x,y)
        if not self.ball and not self.paddle:
            print('shits fucked')
        self.game = game

    def play(self, mode = 'a'):
        memory = self.memory[:]
        self.comp = opComp(memory, outlen=self.outlen)
        self.comp.set_memory(0,2)
        # print(self.ball, self.paddle)
        # test_inp = 'ddsaddddddddddddddddddddddddddddddddddd'

        test = 1
        self.prev = self.ball
        while not self.comp.finished:
            inp = self.smart_paddle()            
            bx,by,id = self.comp.run_prog(inp=inp,ret=True)
            if id == 4:
                self.prev = self.ball
                self.ball = (bx,by)
                t = [each for each in [(bx+1,by),(bx-1,by),(bx,by-1),(bx,by+1)] if each in self.blocks]
                for each in t:
                    self.blocks.remove(each)

            # print(self)
            # time.sleep(1)
            if test > 100 and False:
                break
        else:
            print(f"Exit: {[bx,by,id]}, finsihed: {self.comp.finished}")
            print(len(self.blocks))

    def smart_paddle(self):
        """ 
            if the ball is moving right: dx
                if the paddle is to the right of the future ball:
                    move left
                elif the paddle is to the left of the future ball:
                    move right
                elif the paddle is at the future ball:
                    do nothing
            elif the ball is moving left:
                if the paddle is to the right of the future ball:
                    move left
                elif the padle is to the left of the future ball:
                    move right
                elif the paddle is at the future ball:
                    do nothing

            """
        x1,y1 = self.ball; x2,_ = self.prev; dx = x1-x2
        x,y = self.paddle
        a = 0
        if y1 +1 == y and x1 == x:
            return 0
        elif dx > 0:
            if x > x1 + dx:
                a = -1
            elif x < x1+dx:
                a = 1
        elif dx < 0:
            if x > x1 + dx:
                a = -1
            elif x < x1 + dx:
                a = 1
        self.paddle = (x+a, y)
        return a

    def block_count(self):
        return len(self.blocks)

    def instruction(self):
        return self.comp.output[-self.outlen:]

    def game_dims(self, inst):
        dim = [[],[]]
        for i in inst:
            x,y,_ = i
            if (x,y) != (-1,0):
                dim[0].append(x)
                dim[1].append(y)

        return range( 0, max(dim[0])+1 ), range( 0, max(dim[1])+1 )
            
    
    def __str__(self):
        string = ''
        for y,row in enumerate(self.game):
            for x,_ in enumerate(row):
                if (x,y) in self.blocks:
                    string += '#'
                elif (x,y) == self.paddle:
                    string += '~'
                elif (x,y) == self.ball:
                    string += 'O'
                else:
                    string += ' '
            string += '\n'
        return string



if __name__ == "__main__":
    inst_len = 3
    robot = Robot(outlen=inst_len)

    robot.play()