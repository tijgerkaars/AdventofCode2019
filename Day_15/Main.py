import time
import math
from intComp import opComp
id = 1
t1 = None
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
    def __init__(self, inp = None, outlen = 1, memory = None):
        if memory == None:
            memory = get_input()
        self.memory = memory[:]
        self.comp = opComp(memory[:], outlen=outlen)
        self.outlen = outlen

        self.wall = '#'
        
        self.inp_map = {
                1: 'N',
                2: 'S',
                3: 'W',
                4: 'E' }
        self.inp_map_rev = {
                'S': 1,
                'N': 2,
                'E': 3,
                'W': 4     }
        
        self.directions = list(self.inp_map.keys())

    def run_search(self):
        self.path = []
        self.path_string = ''

        self.start = Tile(self)
        self.oxy = None
        self.start.visited = True
        self.current = self.start

        if False:
            l = 75+10
            for i in range(l):
                r = self.move()
                if i >= l-2:
                    print('\n', self.path)
                    print(f"{'  '} -  prev -- ID: {self.current.prev.id}, {self.current.prev.wall}, {self.current.prev.next}")
                    print(f"{r   } -  curr -- ID: {self.current.id}, {self.current.wall}, {self.current.next}\n")
                    if self.current.next[1]:
                        print(f"{'  '} -  next -- ID: {self.current.next[1].id}, {self.current.next[1].wall}, {self.current.next[1].next}\n")
            return

        counter = 0
        goal = 0
        while goal != -2 and counter < 100000:
            goal = self.move()
            counter += 1
            if goal == 2 and self.path_string == '':
                self.oxy = self.current
                self.path_string = self.clean_path(self.path)
                global t1
                t1 = time.time()
            if goal == -2:
                print(f"returned to start {self.current}")
                break

    def clean_path(self, l):
        l = ''.join(list(map(str, l)))
        for i in range(len(l)-1,2,-1):
            t = l[i-2:i]
            if t in '121 343':
                l = l[:i-2] + l[i:]
        return l

    def bench(self):
        tt0 = time.time()
        for _ in range(10000):
            self.comp.run_prog(1)
        print((time.time()- tt0)/10000)

    def move(self, inp_ = None):
        """ 
            check around => N S W E where no wall & not visited
            if it's marked as a wall:
                skip it
            else:
                if it is the goal:
                    return
                elif a wall is there:
                    mark it
                else:
                    if it is not yet visited:
                        move there
                

            """

        for inp in list(self.current.free):
            if inp_: # if a forced input was used
                inp = inp_
            if inp in self.current.next and self.current.next[inp] == None:
                ins = self.comp.run_prog(inp=inp,ret=True)                       # check if input is good
                if ins == 2:                                                     # if the goal is reached
                    self.path.append( inp )
                    return ins                   
                elif ins == 0:                                                   # if it is a wall
                    self.current.free.remove(inp)
                    self.current.wall.add(inp)                                   # add it to the wall list
                    self.current.next.pop(inp, None)                             # make sure that during backtracking it wont be checked again
                elif ins == 1:                                                   # if it is an available space
                    self.path.append( inp )
                    new_tile = Tile(self, self.current)                          # make a new tile
                    new_tile.next.pop(self.inp_map_rev[self.inp_map[inp]], None) # remove this tile from the options
                    new_tile.free.remove(self.inp_map_rev[self.inp_map[inp]])
                    self.current.free.remove(inp)
                    self.current.next[inp] = new_tile                            # add the new tile to the next options
                    self.current = new_tile                                      # new tile is now current tile
                    # print(f"ins: {ins}, inp: {inp} => new: {new_tile.next}")
                    return ins
            if inp_:
                break
        inp = self.back()
        self.comp.run_prog(inp=inp,ret=True)
        self.path.append( inp )
        
        self.current = self.current.prev
        if self.current == self.start:
            return -2
        return -1

    def back(self):
        t = list(self.current.next.keys()) + list(self.current.wall)
        return [each for each in self.directions if each not in t][0]


    def reshuffel(self):
        self.current = self.oxy
        next_tile = self.oxy.prev
        self.oxy.prev = None
        
        print(self.back())

        counter = 0
        while counter < 300 and self.current != self.start:
            break
            


    """ 
        start at oxy
        move prev to next
        move to prevevious prev, repeat
        
        """

class Tile():
    def __init__(self, robot, prev = None):
        global id
        self.id = id; id += 1
        self.robot = robot
        self.wind_directions = robot.inp_map.keys()

        """
        for each in self.wind_directions:
            exec(f'self.{each} = None')
        """

        self.wall = set()
        self.free = set(self.wind_directions)
        self.next = {each:None for each in self.wind_directions}
        self.prev = prev

    def __repr__(self):
        return str(self.id)


if __name__ == "__main__":
    inst_len = 1
    robot = Robot(outlen=inst_len)
    robot.run_search()

    print('test', len(robot.path_string))

    robot.reshuffel()


    ### p1
    # ans < 440