from pprint import pprint 
from collections import defaultdict

inp = ""
with open('../Data/day16.txt') as infile:
    inp = infile.read()

d = defaultdict(int)

instructions = inp.split(',')

programs = list('abcdefghijklmnop')
# programs = list('abcde')

# instructions = ['s1', 'x3/4', 'pe/b']

def update_dict():
    global programs
    for idx, program in enumerate(programs):
        d[program] = idx
    return 

def spin(num):
    global programs
    l1 = programs[-num:]
    l2 = programs[:-num]
    programs = l1+l2
    update_dict()
    return

def exchange(A,B):
    global programs
    tmp = programs[A]
    programs[A] = programs[B]
    programs[B] = tmp
    update_dict()
    return

def partner(A,B):
    global programs
    idx_A = d[A]
    idx_B = d[B]
    tmp = programs[idx_A]
    programs[idx_A] = programs[idx_B]
    programs[idx_B] = tmp
    d[A] = idx_B
    d[B] = idx_A
    return

def part1():
    for instruction in instructions:
        lst = list(instruction)
        if lst[0] == 's':
            operand = "".join(lst[1:])
            spin(int(operand))
        if lst[0] == 'p':
            partner(lst[1], lst[-1])
        if lst[0] == 'x':
            rest = "".join(lst[1:])
            tmp = rest.split('/')
            exchange(int(tmp[0]), int(tmp[1]))
    return "".join(programs)

def part2():
    d1 = defaultdict(int)
    idx = 0
    for i in range(0,1000000000):
        pprint(i)
        res = part1()
        if res in d1:
            break
        else:
            d1[res] = idx
        idx+=1
    req_idx = (1000000000%idx) - 1
    pprint(req_idx)
    for k,v in d1.items():
        if v == req_idx:
            pprint(k)
    

part2()