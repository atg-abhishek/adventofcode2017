from pprint import pprint 

inp = []

with open('../Data/day5.txt') as infile:
    inp = infile.readlines()

number_lst = list(map(int, inp))
# number_lst = [0,3,0,1,-3]

def part(num):

    escape_max = len(number_lst) - 1
    escape_min = 0
    escaped = False
    jump = number_lst[0]
    idx = 0
    steps = 0 

    while not escaped:
        # pprint("step number + " + str(steps))
        # pprint(number_lst)
        jump = number_lst[idx]
        if num == 2:
            if jump >= 3:
                number_lst[idx] -= 1
            else:
                number_lst[idx] += 1 #increment the existing position by one 
        else:
            number_lst[idx] += 1
        idx += jump
        steps += 1
        if idx < escape_min or idx > escape_max:
            escaped = True
            return steps
        


pprint(part(2))
    
