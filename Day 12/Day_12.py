from collections import defaultdict

f = open('Day_12_Input.txt', 'r')
x = f.read().split('\n')

#default dict is actually amazing
# struggled with this one, had to look up the answer, spent time understanding why it worked. 
# while i didnt write it, i understand it now

caveConnections = defaultdict(list)
for line in x:
    a,b = line.split('-')
    caveConnections[a].append(b)
    caveConnections[b].append(a)



def paths(current, visitedCaves):
    if current == 'end':
        return 1
    if current.islower() and current in visitedCaves:
        return 0
    visitedCaves = visitedCaves | {current}
    numPaths = 0
    for cave in caveConnections[current]:
        numPaths += paths(cave, visitedCaves)
    return numPaths

answer = paths("start", set())
print(answer)

''' part two'''
def paths(current, visitedCaves, secondSmallVisit):
    if current == 'end':
        return 1
    # need this so it doesnt go to start again after the first time
    # basically checking if there have been any visted caves since vistedCaves while return true if there is anything in it
    # so if it does return to start, it end the current function and returns 0 since its not a valid path    
    if current == "start" and visitedCaves:
        return 0
    if current.islower() and current in visitedCaves:
        if secondSmallVisit is None:
            secondSmallVisit = current
        else:
            return 0
    visitedCaves = visitedCaves | {current}
    numPath = 0
    for thing in caveConnections[current]:
        numPath += paths(thing, visitedCaves, secondSmallVisit)
    return numPath

answer = paths("start", set(), None)
print(answer)
