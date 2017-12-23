from pprint import pprint 
from collections import defaultdict

d = defaultdict(int)

instructions = []
with open('../Data/day18.txt') as infile:
    instructions = infile.readlines()

def get_val(inp):
    val = 0
    if inp.isalpha():
        val = d[inp]
    else:
        val = int(inp)
    return val 

last_sound_played = 0 
idx = 0 
while True:
    line = instructions[idx].rstrip()
    pprint(line)
    tmp = line.split(' ')
    if tmp[0] == 'snd':
        last_sound_played = get_val(tmp[1])
    if tmp[0] == 'set':
        d[tmp[1]] = get_val(tmp[2])
    if tmp[0] == 'add':
        d[tmp[1]] += get_val(tmp[2])
    if tmp[0] == 'mul':
        d[tmp[1]] *= get_val(tmp[2])
    if tmp[0] == 'mod':
        d[tmp[1]] = d[tmp[1]] % get_val(tmp[2])
    if tmp[0] == 'rcv':
        if tmp[1].isalpha():
            if d[tmp[1]] > 0:
                print("last sound played is " + str(last_sound_played))
                if last_sound_played > 0:
                    break
        else:
            if int(tmp[1]) > 0:
                print(last_sound_played)
                if last_sound_played > 0:
                    break
    if tmp[0] == 'jgz':
        if get_val(tmp[1]) >0:
            idx += get_val(tmp[2])
            continue
    idx += 1
    if idx >= len(instructions) or idx < 0:
        break


    
    