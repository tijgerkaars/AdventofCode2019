import time

def get_input(test = False):
    if test:
        fn = r"AdventofCode2019\Day_6\test_input.txt"
    else:
        fn = r"AdventofCode2019\Day_6\input.txt"
    with open(fn) as f:
        lines = []
        for line in f:
            lines.append( line.strip())
        if len(lines) == 1:
            lines = lines[0]

        return lines

class ufo():
    def __init__(self, _map, me, parent = None):
        self._map = _map
        self.id = me
        if parent:
            self.parent = parent
            self.orbiting = parent.orbiting + 1
        else:
            self.orbiting = 0


        self.orbitted = []
        orbiters = self.find_orbiters(me)
        for each in orbiters:
            if each == 'YOU':
                _map.ship = _map.walker(self)
            new_ufo = ufo(_map, each, self)
            self.orbitted.append(new_ufo)
            self._map.objects.append(new_ufo)
            
    

    def find_orbiters(self, body):
        orbiters = [each for each in self._map.data if body in each]
        for i, each in enumerate(orbiters):
            self._map.data.remove(each)
            orbiters[i] = orbiters[i].split(')')[1]
        return orbiters

class orbit_map():
    def __init__(self, data):
        self.data = set(data)
        
        self.ship = None
        self.objects = []
        self.center = ufo(self, 'COM')
        total = 0
        for each in self.objects:
            if each.id not in ['YOU', 'SAN']:
                total += each.orbiting
        self.total = total

    class walker():
        def __init__(self, start):
            self.current = start
            self.target = None
            self.jumps = 0

        def travel(self, target = None):
            breaker = 0
            self.target = target
            while breaker < 10000:
                self.move()

                breaker += 1
                if self.target in [each.id for each in self.current.orbitted]:
                    break
            
        def move(self):
            if self.check_branch(self.current):
                self.move_up()
            else:
                self.move_down()
            self.jumps += 1

        def move_up(self):
            for each in self.current.orbitted:
                if self.check_branch(each):
                    self.current = each
                    return
            print('something went wrong')


        def move_down(self):
            self.current = self.current.parent

        def check_branch(self, obj):
            if obj.orbitted:
                if self.target in [each.id for each in obj.orbitted]:
                    return True
                for each in obj.orbitted:
                    if self.check_branch(each):
                        return True
            return False

        
            


if __name__ == "__main__":
    t0 = time.time()
    raw = get_input(test=False)
    m = orbit_map(raw)
    t1 = time.time()
    m.ship.travel('SAN')
    t2 = time.time()
    print(f"Part 1 -- {m.total}, time: {t1-t0:0.4f}S") 
    print(f"Part 2 -- {m.ship.jumps}, time: {t2-t1:0.4f}S") 


""" 
Part 1 -- 122385, time: 0.0530S
Part 2 -- 271, time: 0.0590S
"""