from pprint import pprint 
from collections import defaultdict
inp = []
with open('../Data/day13.txt') as infile:
    inp = infile.readlines()

layers_caught = []

def move_scanners():
    for k,val in d.items():
        if val[1] == 0: 
            continue
        else:
            v = list(val)
            if v[2] == -1: #moving downwards 
                if v[1] < v[0]:
                    v[1] += 1
                else:
                    v[1] -=1 
                    v[2] = 1 #change the direction because we reached the end 
            elif v[2] == 1: #moving upwards
                if v[1] > 1:  
                    v[1] -=1 
                else:
                    v[1] += 1
                    v[2] = -1
            d[k] = tuple(v)
    return 

d = defaultdict(tuple)
max_num = 0
for layer in inp:  #parsing out the input and storing it in a dict with key as the layer number and the value being a tuple with the first entry as the depth and the second entry being the current position of the scanner and the third entry being the direction of motion, -1 is downwards and +1 is upwards
    tmp = layer.split(':')
    layer_number = int(tmp[0])
    depth = int(tmp[1][1:])
    if layer_number>max_num:
        max_num = layer_number
    d[layer_number] = (depth,1, -1)

for i in range(0, max_num+1): #populating the layers that don't have scanners
    if i not in d: 
        d[i] = (0,0,-1) #here the position of the scanner is set as zero because these layers don't have a scanner 

def print_layers():
    lst = []
    for k,v in d.items():
        lst.append(v[1])
    pprint(lst)

def part1():
    for cur_layer in range(0, max_num+1):
        if d[cur_layer][1] == 1:
            layers_caught.append(cur_layer)
        move_scanners()
        # print_layers()
        

    severity = 0
    pprint(layers_caught)
    for lc in layers_caught:
        severity += lc*d[lc][0]

    pprint(severity)

part1()

def compute_future_scanner_positions():
    
    return 

while True:
    min_secs = 0
    for k,v in d.items():
        
    
    move_scanners()
    min_secs += 1