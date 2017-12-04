from pprint import pprint 
from collections import defaultdict
target_number = 347991

def part1():
    i = 3
    square_thickness = 1
    while i*i <= target_number:
        i += 2
        square_thickness += 1

    diff = target_number - (i-2)*(i-2) #tells how far away is the number in this spiral
    # pprint(diff)
    x = 0
    y = 0
    if diff>0 and diff<i: #present on the right side 
        y = diff%i - square_thickness
        x = square_thickness
    else:
        diff+=1
    if diff>=i and diff<2*i: #present on the top side 
        y = square_thickness
        x = diff%i - square_thickness
    else:
        diff+=1
    if diff>=2*i and diff<3*i: #present on the left side 
        x = -square_thickness
        y = diff%i - square_thickness 
    else:
        diff+=1
    if diff>=3*i: #present on the bottom side 
        y = -square_thickness
        x = diff%i - square_thickness

    location = (x,y)
    pprint(location)
    pprint(location[0] + location[1])

def part2():
    d = defaultdict(int)
    x = 1
    y = 0
    val = 0 #initializing the value of val 

    def computeNeighbors(a,b): #finding the neighbors of a given coordinate
        lst = []
        for p in [a-1,a,a+1]:
            for q in [b-1, b, b+1]:
                if (p,q) in d.keys():
                    lst.append((p,q))
        return lst

    def getNext(a,b, width): #used to travel on the spiral 
        if a == width and b== (-width): #case when this square is over
            a+=1
            width+=1
            return (a,b,width)
        
        if a == width: #moving up on the right side
            if b<width:
                b+=1
                return (a,b, width)
                
        if b == width: #moving leftwards on the top side
            if a>(-width):
                a-=1
                return (a,b, width)
                
        if a == (-width): #moving downwards on the left side
            if b>(-width):
                b-=1
                return (a,b, width)
                
        if b == (-width): #moving rightwards on the bottom side 
            if a<width:
                a+=1
                return (a,b, width)
        
    
    square_width = 1
    d[(0,0)] = 1
    while val<=target_number:
        val = 0 #because sum needs to be computed from the new neighbors
        list_of_neighbors = computeNeighbors(x,y)
        for neighbor in list_of_neighbors:
            val += d[(neighbor[0], neighbor[1])]
        d[(x,y)] = val
        (x,y, square_width) = getNext(x,y, square_width)
        
    pprint(val)

part2()