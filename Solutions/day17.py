from pprint import pprint
from blist import blist

def part1():
    inp = 329
    cur_pos = 0
    lst = [0]
    for i in range(1, 2017+1):
        cur_pos = (cur_pos+inp) % len(lst)
        l1 = lst[:cur_pos+1]
        l2 = lst[cur_pos+1:]
        lst = l1 + [i] + l2
        cur_pos += 1

def part2(): #using more efficient implementation of lists that allows for O(log n) insert times 
    inp = 329
    cur_pos = 0
    lst = blist([0])
    for i in range(1, 50000000+1):
        cur_pos = (cur_pos+inp) % len(lst)
        lst.insert(cur_pos+1, i)
        cur_pos += 1
    for idx, item in enumerate(lst):
        if item==0:
            pprint(lst[idx+1])
    
part2()