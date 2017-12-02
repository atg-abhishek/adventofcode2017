from pprint import pprint 

inp = ""
with open('../Data/day1.txt') as infile:
    inp = infile.read()

def part1():
    circularString = inp + inp[0] #adding the first digit at the end to do circular analysis

    total = 0
    for idx, val in enumerate(circularString[:-1]):
        if int(val) == int(circularString[idx+1]):
            total += int(val)

    pprint(total)

def part2():
    total = 0
    length = len(inp)
    for idx, val in enumerate(inp):
        jump = idx+len(inp)/2
        if jump>=len(inp):
            jump = jump%len(inp)
        jump = int(jump)
        if int(val) == int(inp[jump]):
            total += int(val)
    pprint(total)

part2()