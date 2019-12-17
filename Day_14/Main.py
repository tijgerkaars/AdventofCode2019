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
                lines.append( line.strip())
            if len(lines) == 1:
                lines = lines[0]

            return lines

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


class Reactor():
    def __init__(self, inp, fuel = 1):
        self.test = False

        self.fuel = fuel

        self.recipies = self.Build_Recipie_dict(inp)
        self.Calc_Cost()

    def Build_Recipie_dict(self, inp):
        recipies = dict()
        for each in inp:
            if 'FUEL' in each or True:
                req, res = each.split(' => ')
                val, key = res.split(' ')
                recipies[key] = [int(val), req.split(', ')]
        return recipies

    def Calc_Cost(self):
        recipies = self.recipies
        cost = 0
        required = list(recipies.keys()) + ['ORE']
        self.required = {each:0 for each in required}; self.required['FUEL'] = self.fuel
        self.left     = {each:0 for each in required}
        self.produced = {each:0 for each in required}

        self.Resolve_Recipie(self.Next_Eq())

        counter = 0
        while not self.Finished() and counter < 100000:
            self.Resolve_Recipie(self.Next_Eq())
            counter += 1
        return cost

    def Next_Eq(self):
        for key,value in self.required.items():
            if key != 'ORE':
                if value > 0 :
                    return key


    def Finished(self):
        for key,value in self.required.items():
            if key != 'ORE':
                if value > 0 :
                    return False
        return True

    def Resolve_Recipie(self, recipie):
        equation = self.recipies[recipie]
        needed = self.required[recipie]; left = self.left[recipie]
        # check if prodcution is needed
        if left >= needed:
            self.left[recipie] -= needed
            self.required[recipie] = 0
            remainder = 0
            return
        else:
            # see how much production is needed
            remainder = needed - left
            self.required[recipie] = 0
            self.left[recipie] = 0
            
        yields, consumes = equation
        reactions = modish(remainder,yields)
        if self.test:
            print(f"Start: {self.required}\n       {self.left}")
            print(f"Remainder: {remainder}")
            print(f"Reaction : {yields} {recipie} requires: { consumes}\n")

            print(f"Reactions needed: {reactions}\n")
        
        for each in consumes:
            amount, chem = each.split(); amount = int(amount)
            self.required[chem] += reactions * amount
            self.produced[chem] += reactions * amount
        self.left[recipie] += reactions*yields-remainder
        
def modish(a,b):
    return a//b + int(a%b!=0)

def modish_(a,b):
    i = 1
    while a > b:
        a -= b; i += 1
    return i



if __name__ == "__main__":
    from time import time
    t0 = time()

    inp = get_input(test=False)       

    reactor = Reactor(inp)
    part1 = reactor.required['ORE']
    print(part1)
    t1 = time()


    part2 = 0; low = 0; high = 10**12
    ore_max = 10**12
    counter = 0

    condition = high - low
    while high - low != 1:
        f = (high-low)/2 + low

        reactor2 = Reactor(inp,fuel=f)
        ore = reactor2.required['ORE']
        
        if ore > ore_max:
            high = f
        elif ore < ore_max:
            low = f
        if ore == ore_max:
            break


        counter += 1
        if counter % 100 == 0:
            print(f"Ore: {ore:0.4E}, Fuel: {f:0.4E}, High: {high:0.2E}, Low: {low:0.2E}, Diff: {high-low}, Goal: {ore - ore_max}")

        if high-low == condition:
            print(f"Ore: {ore:0.4E}, Fuel: {f:0.4E}, High: {high:0.2E}, Low: {low:0.2E}, Diff: {high-low}, Goal: {ore - ore_max}")
            print(high,low,sep='\n')
            break
        else:
            condition = high-low

       

    print(f"fuel: {f:.0f}")
   
    
    
    
    t2 = time()
    print(t2-t1)

    # ans > 70236
    # ans < 82892752