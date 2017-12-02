from pprint import pprint 

lst = []
with open('../Data/day2.txt') as infile:
    lst = infile.readlines()

def part1():
    total = 0
    for item in lst:
        numbers_list = list(map(int, item.split("\t")))
        diff = max(numbers_list) - min(numbers_list)
        total += diff

    pprint(total)

def part2():
    total = 0
    # lst = [[5,9,2,8], [9,4,7,3], [3,8,6,5]]
    for item in lst:
        numbers_list = list(map(int, item.split("\t")))
        # numbers_list = item
        for idx, n in enumerate(numbers_list[:-1]):
            for m in numbers_list[idx+1:]:
                if n>m:
                    if n%m==0:
                        total+= int(n/m)
                else:
                    if m%n==0:
                        total+=int(m/n)
    pprint(total)

part2()