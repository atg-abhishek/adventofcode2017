from pprint import pprint 
from collections import defaultdict

d = defaultdict(int)
s = set()

for letter in list('abcdefgh'):
    d[letter] = 0

d['a'] = 1

instructions = []
with open('../Data/day23.txt') as infile:
    instructions = infile.readlines()

idx = 0
count = 0 

def get_val(inp):
    val = 0
    if inp.isalpha():
        val = d[inp]
    else:
        val = int(inp)
    return val 

while True:
    line = instructions[idx].rstrip()
    tmp = line.split(' ')
    
    # try creating a dict with the instruction and state of d because there might be cycles 
    lst = []
    for k,v in d.items():
        lst.append(k)
        lst.append(v)
    pair = tuple(tmp + lst)
    if pair in s:
        break
    else:
        s.add(pair)

    if tmp[0] == 'set':
        val = get_val(tmp[2])
        d[tmp[1]] = val
    if tmp[0] == 'sub':
        val = get_val(tmp[2])
        d[tmp[1]] -= val
    if tmp[0] == 'mul':
        val = get_val(tmp[2])
        d[tmp[1]] *= val 
        count += 1
    if tmp[0] == 'jnz':
        x = get_val(tmp[1])
        if x != 0:
            idx += get_val(tmp[2])
            continue
    idx+=1
    if idx >= len(instructions) or idx < 0:
        break

pprint(d['h'])