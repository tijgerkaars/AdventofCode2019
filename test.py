
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


r1 = range(11)
r2 = range(10,-1,-1)

l = [i for i in r1] + [i for i in r2]

print(l)
