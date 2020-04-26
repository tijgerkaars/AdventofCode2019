p = print

def mult_map(t):
    a,b = t
    return a*b

phases = 100

test1 = False
test2 = False

if test1:
    inp = '80871224585914546619083218645595'; test_out = '24176176'
    inp = '19617804207202209144916044189917'; test_out = '73745418'
    inp = '69317163492948606335995924319873'; test_out = '52432133'
    # inp = [f'{i}' for i in range(1,9)] ; test_out = '48226158'
    offset = 1
    inp_repeat = 1
elif test2:
    inp = '03036732577212944063491565474664'; test_out = '84462026'
    offset = int(''.join(inp[:8]))
    inp_repeat = 10000
else:
    inp_repeat = 10000
    inp = '59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608'
    offset = int(''.join(inp[:8]))


inp = list(map(int,inp))
inp *= inp_repeat

inp_len = len(inp)

print(f"offset= {offset}, inp_repeat= {inp_repeat}\ninp_len= {inp_len}, inp= {inp if test1 == True else None}")

# much to slow
pattern = [0, 1, 0, -1]

for t in range(phases):
    print(phases-t)
    output = []
    for index in range(inp_len//2, 1+inp_len):
        sum_out = 0
        for j in range(inp_len//2, inp_len):
            sum_out += (pattern[((j+offset)//index)%4] * inp[j])
        output.append(abs(sum_out)%10)
    inp = output


s_out = ''.join(map(str,output[:8]))
print(f"output = {s_out}, should be {test_out}")
print(s_out == test_out)

 """