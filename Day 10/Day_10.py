from statistics import median
f = open('Day_10_Input.txt', 'r')
x = f.read().split('\n')
data = []
for i in range(len(x)):
    data.append([])
    for char in x[i]:
        data[i].append(char)

# pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
# wrongWay = [')', ']', '}', '>']
# pointTable = {')': 3, ']': 57, '}': 1197, '>': 25137}
# points = 0
# for line in data:
#     nl = line
#     match = True
#     while match:
#         for index in range(len(nl)):
#             char = nl[index]
#             if char in wrongWay:
#                 findChar = pairs[char]
#                 check = nl[index - 1]
#                 if check == findChar:
#                     nl.pop(index)
#                     nl.pop(index - 1)
#                     break
#                 else:
#                     match = False
#                     points += pointTable[char]
#                     break
#         for y in wrongWay:
#             if y not in nl:
#                 shouldBreak = True
#             else:
#                 shouldBreak = False
#                 break
#         if shouldBreak:
#             break
# print(points)

'''part two'''
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
revPairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
wrongWay = [')', ']', '}', '>']
count = 0
pointTable = {')': 1, ']': 2, '}': 3, '>': 4}
points = 0
lines = []
for line in data:
    nl = line
    count += 1
    match = True
    while match:
        for index in range(len(nl)):
            char = nl[index]
            if char in wrongWay:
                findChar = pairs[char]
                check = nl[index - 1]
                if check == findChar:
                    nl.pop(index)
                    nl.pop(index - 1)
                    break
                else:
                    match = False
                    points += pointTable[char]
                    break
        for y in wrongWay:
            if y not in nl:
                shouldBreak = True
            else:
                shouldBreak = False
                break
        if shouldBreak:
            lineScore = ''
            for c in range(len(nl) - 1, -1, -1):
                lineScore += revPairs[nl[c]]
            lines.append(lineScore)
            break

points = []
for line in lines:
    pointTotal = 0
    for char in line:
        pointTotal *= 5
        pointTotal += pointTable[char]
    points.append(pointTotal)
print(median(points))