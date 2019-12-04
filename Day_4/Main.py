import time
t1 = time.time()


from collections import Counter

def valid_num(number, l):
    num_p = [int(each) for each in str(number)]
    matching = False
    for i in range(l-1):
        n1, n2 = num_p[i:i+2]
        if n1 > n2:
            return False
        if n1 == n2:
            matching = True
    return matching

def valid_num_2(number, l):
    num_p = [int(each) for each in str(number)]
    values = list(Counter(num_p).values())
    if values.count(2) > 0:
        return True
    return False








puzzle_input = (136760,595730)

passwords = []
l = 6

lo,up = puzzle_input
for p in range(lo,up):
    if valid_num(p, l):
        passwords.append(p)
t2 = time.time()

new_passwords = []
for each in passwords:
    if valid_num_2(each,l):
        new_passwords.append(each)



print(f"Part 1 -- {len(passwords)}, t: {t2-t1:.4f}")
print(f"Part 2 -- {len(new_passwords)}, t: {time.time() - t2:.4f}")
print(f"Total time: {time.time()-t1}")