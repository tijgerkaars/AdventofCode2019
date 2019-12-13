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
    def __init__(self):
        memory = get_input()
        self.comp = opComp(memory)
        
        self.pos = (0,0)
        self.dir = '^'
        self.visited = []

        self.move_logic = {
            '^': { 0 : '<', 1 : '>' },
            '>': { 0 : '^', 1 : 'v' }, 
            'v': { 0 : '>', 1 : '<' }, 
            '<': { 0 : 'v', 1 : '^' }
            }

        self.pos_logic = {
            '^': ( 0,-1),
            '>': ( 1, 0),
            'v': ( 0, 1),
            '<': (-1, 0)
            }

        self.white = set()
    
    def run(self, inp = None):
        self.move(inp=inp)
        counter = 0
        while self.running() and counter < 100000:
            self.move()
            counter += 1
        # self.move()

    def paint(self, color):
        if color:
            self.white.add(self.pos)
        elif self.pos in self.white:
            self.white.remove(self.pos)

    def running(self):
        return not self.comp.finished

    def move(self, inp = None):
        if inp != None:
            self.paint(inp)
            self.comp.run_prog( inp = inp )
        else:
            self.comp.run_prog( inp = int(self.pos in self.white) )

        color, direction = self.instruction()
        # --- paint ---
        self.paint(color)
        # ---  move ---
        self.visited.append(self.pos)
        self.dir = self.move_logic[self.dir][direction]
        self.update_pos()
        # print(self.visited[-1], self.white)
    
    def update_pos(self):
        x,y = self.pos
        dx,dy = self.pos_logic[self.dir]
        self.pos = (x+dx, y+dy)
   
    def instruction(self):
        return self.comp.output[-2:]

    def panel_check(self):
        return len(set(self.visited))

    def show_drawing(self):
        X = [0]; Y = [0]
        for each in self.white:
            x,y = each
            X.append(x); Y.append(y)
        xRange = range(min(X), max(X)+1)
        yRange = range(min(Y), max(Y)+1)

        string = ''
        for y in yRange:
            for x in xRange:
                if (x,y) in self.white:
                    string += '#'
                else:
                    string += ' '
            string += "\n"
        print(string)



if __name__ == "__main__":
    from time import time
    t0 = time()
    robot1 = Robot()
    robot1.run()
    part1 = robot1.panel_check()
    t1 = time()
    print(f"Part 1 -- {part1}, t: {t1-t0}")
    
    robot2 = Robot()
    robot2.run(1)
    print(robot2.comp.opcodes_run)
    print(f"Part 2 -- \n")
    robot2.show_drawing()
    t2 = time()
    print(f"t: {t2-t1}")
    print(f"total time {t2-t0}")


# not 
# PFKHFR7I
# PFKHFr7l