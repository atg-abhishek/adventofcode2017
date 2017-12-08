from pprint import pprint 
from collections import defaultdict, Counter

d = defaultdict(list)
raw_list = []
with open('../Data/day7.txt') as infile:
    raw_list = infile.readlines()

for node in raw_list:
    items = node.split(" ")
    source_node = items[0]
    weight = items[1]
    if '\n' in weight:
        weight = int(items[1][1:-2]) #getting rid of the parenthesis and trailing \n
    else:
        weight = int(items[1][1:-1])
    nodes_on_top = []
    leaf = True
    if len(items) > 2: #it has other nodes on top of it 
        for item in items[3:-1]:
            nodes_on_top.append(item[:-1]) #getting rid of the comma
        nodes_on_top.append(items[-1][:-1]) #getting rid of the trailing \n
        leaf = False
    weight = [weight,0] #the second item represents the weight above 
    back_nodes = []
    d[source_node] = [back_nodes, weight, nodes_on_top, leaf]

for x in list(d): #not using d.items() because you can't then modify the things in the iterator while using it, you get a dictionary changed size during iteration problem 
    if not d[x][-1]: #not a leaf node 
        nodes_on_top = d[x][-2]
        for node in nodes_on_top:
            d[node][0].append(x)

def part1():
    for x in list(d):
        if len(d[x][0]) == 0:
            pprint(x)

def check_sub_tower_weights(li): 
    # pprint("the list in sub tower check is " + str(li))
    weight_dict = defaultdict(list) #dict with weights as the key and the list of nodes that have that weight 
    for item in li:
        weight_dict[d[item][1][0] + d[item][1][1]].append(item)
    pprint(weight_dict)
    for idx, w in enumerate(list(weight_dict)):
        if len(weight_dict[w]) == 1:
            required_weight_difference = list(weight_dict)[idx-1] - w
            erring_node = weight_dict[w][0]
            return (erring_node, d[erring_node][1][0] + required_weight_difference ) #the node that has the unique weight and the required weight 
    
    

    return 0 #all the weights aligned

temp_dict = {}

def check_balance(li):
    temp_dict = {}
    for node in li:
        pprint(node)
        # pprint(temp_dict)
        if len(d[node][0]) > 0: #to check that we haven't reached the bottom node 
            parent_node = d[node][0][0]
            if parent_node not in temp_dict:
                # pprint("new parent " + parent_node)
                temp_dict[parent_node] = d[parent_node]
                nodes_on_top = d[parent_node][-2]
                weights_above = 0
                if len(nodes_on_top) > 0:
                    for n in nodes_on_top:
                        weights_above += d[n][1][0]
                # d[parent_node][1][1] += weights_above
                # pprint("parent node is " + str(d[parent_node]))
                res = check_sub_tower_weights(nodes_on_top)
                # pprint("res is " + str(res)) 
                if res != 0:
                    pprint("time to break out ")
                    pprint(res)
                    return res
                else:
                    # pprint("continued")
                    continue
        else:
            return "Failure"
    pprint("***************************************************about to start recursive step ")
    pprint(temp_dict)
    check_balance(list(temp_dict))

leaves = []
for x in list(d):
    if d[x][-1]:
        leaves.append(x)

# pprint(len(leaves))

pprint(check_balance(leaves))
# pprint(d['dkcqdx'])