from pprint import pprint 
from collections import defaultdict
import copy 

d = defaultdict(tuple)
inp = []

with open('../Data/day12.txt') as infile:
    inp = infile.readlines()

for instruction in inp:
    instruction = instruction.rstrip() #removing trailiing newline 
    instruction = instruction.replace(" ", "") #remove all whitespaces
    tmp = instruction.split('<->')
    d[int(tmp[0])] = tuple(list(map(int, tmp[1].split(','))))

s = set()
temp_dict = copy.deepcopy(d)
cur_size = len(s)
iter_num = 1

while True: #need to keep looping through the entries to discover new connections till the size of the set doesn't grow anymore 

    for k,v in d.items():
        if k == 0:  #all the items connected directly to zero need to be added 

            s.add(k) #adding zero itself 
            for val in v:  #all the values directly connected 
                s.add(val)
                
                items = temp_dict[val] #find the items now connected directly with these values as they will be the second-degree connections 
                for item in items:
                    s.add(item)
        else:
            if k in s: #this will act as a second-degree connection
                for val in v: #adding all the values connected to this to zero because the key is connected to zero 
                    s.add(val)
                    items = temp_dict[val] #checking all the nodes that are connected to this node and adding those in 
                    for item in items:
                        s.add(item)
            else:
                connection = False
                for val in v:
                    if val in s:
                        connection = True
                        break
                if connection:
                    for val in v:
                        s.add(val)
                        items = temp_dict[val]
                        for item in items:
                            s.add(item)
    pprint(" Iter num " + str(iter_num) + " completed")
    iter_num += 1
    if len(s) == cur_size:
        break
    else:
        cur_size = len(s)

pprint(len(s))
