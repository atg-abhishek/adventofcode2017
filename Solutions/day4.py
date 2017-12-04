from pprint import pprint 
from collections import defaultdict
lst = []
with open('../Data/day4.txt') as infile:
    lst = infile.readlines()

def part1():
    count = 0
    for passphrase in lst:
        s = set()
        duplicates = False
        words = passphrase.split(" ")
        words[-1] = words[-1].split("\n")[0]
        for word in words:
            if word in s:
                duplicates = True
                break
            s.add(word)
        if not duplicates:
            count += 1
            pprint(words)

    pprint(count)

def part2():
    total_count = 0
    
    def check_anagrams(li):
        letters_list = [] #will store dict of all the words and their letter counts 
        for word in li: #creating a dict with all the letter counts for the word 
            d = defaultdict(int)
            lett_list = list(word) #separating out all the letters
            for letter in lett_list:
                if letter in d.keys(): #check if letter has already been added to the list 
                    d[letter] = d[letter] + 1 #if yes then increment the count by 1
                else:
                    d[letter] = 1 #if not create a new entry 
            letters_list.append(d) #adding this dictionary to the letters list 

        anagram_found = False
        for idx, dictionary in enumerate(letters_list):
            # each dictionary represents one word 
            for d in letters_list[idx+1:]: #comparing this word with all the other words
                if len(d.keys())!=len(dictionary.keys()): #if they don't have the same number of unique letters no point checking forward
                    continue
                else:
                    broken = False #flag to check for a complete match 
                    for k,v in d.items():
                        if k not in dictionary.keys(): #if the letters don't match up no point checking further
                            broken = True
                            break
                        else:
                            if dictionary[k] != v: #if the count of the matched letters doesn't match, then we break 
                                broken = True 
                                break
                    if not broken: #if it wasn't broken, then all letters matched with their counts 
                        anagram_found = True
                        break
        
        return anagram_found



    for passphrase in lst:
        words = passphrase.split(" ")
        words[-1] = words[-1].split("\n")[0]
        if not check_anagrams(words):
            total_count +=1 
    pprint(total_count)


part2()
        
    
