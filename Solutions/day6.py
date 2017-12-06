from pprint import pprint 
from itertools import repeat
import operator
from collections import defaultdict
inp = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14".split('\t')
numbers_lst = list(map(int, inp))
# numbers_lst = [0,2,7,0]

def reorganize(li):
    max_idx = li.index(max(li))
    max_elem = max(li)
    list_of_indices = list(range(max_idx+1, len(li))) + list(range(0,max_idx+1)) #creating the list of indices over which we need to iterate
    li[max_idx] = 0

    num = int(max_elem/len(li))
    if num>=1: #the following piece of code is useful to generate copies of the list of indices to continue placing the numbers into different places till we run out, when num is more than 1 we know that we'll have to loop over multiple times 
        list_of_indices = list(repeat(list_of_indices,num+1))
        list_of_indices = [item for sublist in list_of_indices for item in sublist] #flattening the list of lists 
    # pprint(list_of_indices)
    for i in list_of_indices:
        if max_elem != 0:
            li[i] += 1
            max_elem -= 1
        else:
            break
    return li

count = 0
s = defaultdict(int)
s[tuple(numbers_lst)] = count
pattern_found = False

def part1():
    global numbers_lst, count
    while not pattern_found:
        res = reorganize(numbers_lst)
        if tuple(res) in s:
            break
        count += 1
        numbers_lst = res
        s[tuple(numbers_lst)] = count

part1()
pprint("****************" + str((count+1) - s[tuple(numbers_lst)]))
