from pprint import pprint 
from collections import defaultdict
import operator
import sys
instructions_list = []

with open('../Data/day8.txt') as infile:
    instructions_list = infile.readlines()

registers = defaultdict(int)
overall_max = -sys.maxsize-1
for instruction in instructions_list:
    pieces = instruction.split(" ")
    register_name = pieces[0]
    operation = pieces[1]
    operand = pieces[2]
    op1 = pieces[4]
    condition_operator = pieces[5]
    op2 = pieces[6]

    if register_name not in registers:
        registers[register_name] = 0

    op1_value = registers[op1]
    condition = str(op1_value) + " " + condition_operator + " " + op2
    if eval(condition):
        if operation == "inc":
            registers[register_name] += int(operand)
        if operation == "dec":
            registers[register_name] -= int(operand)
    
    temp = registers[register_name]
    if temp> overall_max:
        overall_max = temp


max_val = max(registers.items(), key=operator.itemgetter(1))[1]  
pprint(max_val)
pprint(overall_max)