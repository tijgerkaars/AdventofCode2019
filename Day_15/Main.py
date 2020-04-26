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
    def __init__(self, inp = None, memory = None, outlen = 1):
        self.wall = Tile()

        self.pos     = (0,0)
        self.root    = Tile(  )
        self.current = Tile( (self.pos) )
        self.root.next.append(self.current)
        self.current.previous = self.root


        self.grid = { self.pos : self.current}
        self.path = []
        
        if inp == None:
            inp = get_input(r'Day_15\input.txt')
        self.inp = inp

        self.brain = opComp(memory=self.inp[:], outlen=outlen)

        self.num_commands     = { 1 : 'n',     2 : 's',     3 : 'w',     4 : 'e'}
        self.commands         = {'n':  1,     's':  2,     'w':  3,     'e':  4}
        self.reverse_commands = {'n': 's',    's': 'n',    'w': 'e',    'e': 'w'} 
        self.coords           = {'n':(0,-1),  's':(0,1),   'w':(-1,0),  'e':(1,0)}

        self.run()

    def run(self):
        ### Handels exploration
            # once the robot returns to the starting point and no more untried directions remain   
            #    try all directions
            #      if no move is made 
            #          add a wall tile
            #      elif a move is made
            #          if that tile was already visited
            #              link and move back
            #          else
            #              make a new tile and link it
            ###
            # count steps down
            # start counting steps up once code 2 is returned by opcomp
            # once all paths are found,
            #   track back through the paths that have no count yet
        
        failsave = 0; test_runs = 1

        while failsave < test_runs:
            failsave += 1
            for i in self.num_commands.keys():
                move_result = self.brain.run_instruction(inp=i, ret=True)
                if move_result in [1,2]:
                    self.path.append(i)
                    print(move_result)
                    break


class Tile():
    def __init__(self, pos = None):
        self.pos = pos
        self.directions = 'nesw'
        self.steps = None

        self.neigbours = {d:None for d in self.directions}   # tracks neighbours
        
        self.previous = None
        self.unexplored = set(self.directions)
        self.next = []
    
    def reset(self):
        self.unexplored = set(self.directions)
        self.next = []

    def unlinked(self):
        return [key for key,value in self.neigbours.items() if value == None]

    def linked(self):
        # returns true if all neighbours are explored
        return [key for key,value in self.neigbours.items() if value != None]



robot = Robot()