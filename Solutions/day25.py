from pprint import pprint 
from collections import defaultdict

req_steps = 12964419
# req_steps = 10

d = defaultdict(int) #key is the position and value is 0 or 1 

cur_pos = 0
d[cur_pos] = 0
count = 0 

def stateA():
    global cur_pos
    if d[cur_pos] == 0:
        d[cur_pos] = 1
        cur_pos += 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'B'
    if d[cur_pos] == 1:
        d[cur_pos] = 0
        cur_pos += 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'F'

def stateB():
    global cur_pos
    if d[cur_pos] == 0:
        d[cur_pos] = 0
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'B'
    if d[cur_pos] == 1:
        d[cur_pos] = 1
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'C'

def stateC():
    global cur_pos
    if d[cur_pos] == 0:
        d[cur_pos] = 1
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'D'
    if d[cur_pos] == 1:
        d[cur_pos] = 0
        cur_pos += 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'C'

def stateD():
    global cur_pos
    if d[cur_pos] == 0:
        d[cur_pos] = 1
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'E'
    if d[cur_pos] == 1:
        d[cur_pos] = 1
        cur_pos += 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'A'

def stateE():
    global cur_pos
    if d[cur_pos] == 0:
        d[cur_pos] = 1
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'F'
    if d[cur_pos] == 1:
        d[cur_pos] = 0
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'D'

def stateF():
    global cur_pos
    if d[cur_pos] == 0:
        d[cur_pos] = 1
        cur_pos += 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'A'
    if d[cur_pos] == 1:
        d[cur_pos] = 0
        cur_pos -= 1
        if cur_pos not in d:
            d[cur_pos] = 0
        return 'E'

# pprint(d)
res = stateA() #begin in state A 

while count<req_steps-1: #because state A has been run once to kickstart the process 
    # pprint(d)
    # pprint("cirpos " + str(cur_pos))
    # pprint("state is " + res)
    if res == 'A':
        res = stateA()
        count += 1
        continue
    if res == 'B':
        res = stateB()
        count += 1
        continue
    if res == 'C':
        res = stateC()
        count += 1
        continue
    if res == 'D':
        res = stateD()
        count += 1
        continue
    if res == 'E':
        res = stateE()
        count += 1
        continue
    if res == 'F':
        res = stateF()
        count += 1
        continue

total = 0
for k,v in d.items():
    total += v

pprint(total)