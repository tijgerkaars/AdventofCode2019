import numpy as np
from math import gcd
from functools import reduce



def get_input(test = False):
    if test:
        name = r'AdventofCode2019\Day_12\test_input.txt'
    else:
        name = r'AdventofCode2019\Day_12\input.txt'
    with open(name) as f:
        lines = []
        for line in f:
            l = line.strip()
            l = [each for each in l if each not in '<>= yxz']
            l = [int(each) for each in ''.join(l).split(',')]
            lines.append(l)
        if len(lines) == 1:
            lines = lines[0]
        return lines

def lcm(a, b):
  return (a * b) // gcd(a, b)

class Sim():
    def __init__(self, moons):
        self.starting_condition = moons.copy()
        self.moons = moons.copy()
        self.tot = None
        self.steps = 0

    def run(self, frames = 10, debug=False):
        if debug:
            frames = 2
        for _ in range(frames):
            self.update()
        return self.calc_en_tot()
    
    
    def calc_en_tot(self):
        self.tot = sum(self.calc_en_pot() * self.calc_en_kin())
        return self.tot

    def update(self):
        self.steps += 1
        self.reset_acc()
        
        self.calc_acc()
        self.calc_vel()
        self.calc_pos()

    def run_cycle(self):
        start = self.starting_condition[:,0,:]
        sxyz = [start[:,0], start[:,1], start[:,2]]

        matches = dict()
        while len(matches) < 3:
            self.update()
            current = self.moons[:,0:2]
            cxyz= [current[:,0,0], current[:,0,1], current[:,0,2] ]
            for i in range(3):
                if i not in matches:
                    if np.array_equal(sxyz[i], cxyz[i]):
                        matches[i] = self.steps +1 
        return reduce(lcm, matches.values())


    def calc_en_pot(self):
        return np.sum(abs(self.moons[:,0]),axis=1)

    def calc_en_kin(self):
        return np.sum(abs(self.moons[:,1]),axis=1)


    def calc_pos(self):
        self.moons[:,0] += self.moons[:,1]

    def calc_vel(self):
        self.moons[:,1] += self.moons[:,2]

    def reset_acc(self):
        self.moons[:,2,:] = 0

    def calc_acc(self):
        for i, _ in enumerate(self.moons):
            current = self.moons[i]
            acc = self.moons[:,0,:] - current[0]
            acc_min  = np.where(acc<0, -1, 0)
            acc_max  = np.where(acc>0,  1, 0)
            acc_new = acc_max[:] + acc_min[:]
            acc_new = np.sum(acc_new, axis=0)
            current[2] = acc_new


    def __str__(self):
        print('\n=====================')
        print("     x,   y,   z\n---------------------")
        print(self.moons)
        print('\n=====================')
        return ''

if __name__ == "__main__":
    from time import time
    t0 = time()

    state = False; cycles = 10000
    inp = get_input(test=state)     
    dims = 3
    moons = np.zeros((len(inp), 3, dims)) 

    """  moons(id,type,vector)

        type: 0 = pos
              1 = vel
              2 = acc

        vec : 0 = x
              1 = y
              2 = z
        """
    for i, each in enumerate(inp):
        moons[i,0,:] = np.array(each)
    sim = Sim(moons)
    sim.run(cycles, debug=state)
    part1 = sim.tot
    t1 = time()


    sim = Sim(moons)
    part2 = sim.run_cycle()

    if state:
        print(4686774924 == part2)

    t2 = time()

    print(f'Part 1 -- {part1}, t: {t1-t0}')
    print(f'Part 2 -- {part2}, t: {t2-t1}')
    print(f'total  -- t: {t2-t1}')


    # ans < 2836259668742993
