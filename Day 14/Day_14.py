from collections import defaultdict
f = open('Day_14_Input.txt', 'r')
x = f.read().split('\n\n')
polyTem = x[0]
rawRules = x[1].split('\n')
rules = {}
for line in rawRules:
    rule = line.split('->')
    rules[rule[0].strip()] = rule[1].strip()

updatedTemp = polyTem[0]
for i in range(10):
    updatedTemp = polyTem[0]
    for index in range(len(polyTem) - 1):
        pair = polyTem[index] + polyTem[index + 1]
        updatedTemp += rules[pair] + pair[1]
    
    polyTem = updatedTemp
    
letterCount = defaultdict(int)
for letter in polyTem:
    letterCount[letter] += 1

answer = max(letterCount.values()) - min(letterCount.values())
print(answer)

'''part two'''
polyTem = x[0]
pairs = defaultdict(int)
for index in range(len(polyTem) - 1):
        pair = polyTem[index] + polyTem[index + 1]
        pairs[pair] += 1
for i in range(40):
    newPairs = defaultdict(int)
    for key, value in pairs.items():
        keyPair = rules[key]
        newPairs[key[0] + keyPair] += value
        newPairs[keyPair + key[1]] += value
    pairs = newPairs

letters = defaultdict(int)
letters['B'] += 1
for k, v in pairs.items():
    letters[k[1]] += v

answer2 = max(letters.values()) - min(letters.values())
print(answer2)

''' Since i am using the second letter of each pair to count the number of letters, I need to give the very first letter an extra 1 because it is skipped over.'''