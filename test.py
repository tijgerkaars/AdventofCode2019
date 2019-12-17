
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def modish(a,b):
    print(a//b + int(a%b!=0))

def modish_(a,b):
    i = 1
    while a > b:
        a -= b; i += 1
    return i

print(modish(17,8))


print(
    82892753 - 82892752
)