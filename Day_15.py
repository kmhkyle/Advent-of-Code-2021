from collections import defaultdict
f = open('Day_15_Input.txt', 'r')
grid = f.read().split('\n')

cavernWidth = len(grid[0])
cavernLength = len(grid)
vertDistances = {(0, 0): 0}
adjacentVerts = {(0, 0): []}

def findAdjacent(currentAdjacents):
    updatedAdj = defaultdict(list)
    for vert in currentAdjacents.keys():
        Y = vert[0]
        X = vert[1]
        if Y == 0:
            if X == 0:
                checkEast(Y, X, updatedAdj)
                checkSouth(Y, X, updatedAdj)
            elif X == cavernWidth - 1:
                checkWest(Y, X, updatedAdj)
                checkSouth(Y, X, updatedAdj)
            else:
                checkEast(Y, X, updatedAdj)
                checkSouth(Y, X, updatedAdj)
                checkWest(Y, X, updatedAdj)
        elif Y == cavernLength - 1:
            # dont need to check right, bottom edge since thats where we want to be
            if X == 0:
                checkNorth(Y, X, updatedAdj)
                checkEast(Y, X, updatedAdj)
            else:
                checkNorth(Y, X, updatedAdj)
                checkEast(Y, X, updatedAdj)
                checkWest(Y, X, updatedAdj)
        elif X == 0:
            checkNorth(Y, X, updatedAdj)
            checkEast(Y, X, updatedAdj)
            checkSouth(Y, X, updatedAdj)
        elif X == cavernWidth - 1:
            checkNorth(Y, X, updatedAdj)
            checkWest(Y, X, updatedAdj)
            checkSouth(Y, X, updatedAdj)
        else:
            checkNorth(Y, X, updatedAdj)
            checkEast(Y, X, updatedAdj)
            checkSouth(Y, X, updatedAdj)
            checkWest(Y, X, updatedAdj)         
    currentAdjacents = updatedAdj
    return currentAdjacents

def checkNorth(Y, X, dict):
    if (Y - 1, X) not in vertDistances:
        return dict[(Y, X)].append((Y - 1, X))

def checkEast(Y, X, dict):
    if (Y, X + 1) not in vertDistances:
        return dict[(Y, X)].append((Y, X + 1))

def checkSouth(Y, X, dict):
    if (Y + 1, X) not in vertDistances:
        return dict[(Y, X)].append((Y + 1, X))

def checkWest(Y, X, dict):
    if (Y, X - 1) not in vertDistances:
        return dict[(Y, X)].append((Y, X - 1))

adjacentVerts = findAdjacent(adjacentVerts)
for k, v in adjacentVerts.items():
    keyDist = vertDistances[k]
    for vert in v:
        print(vert)
        print(grid[vert[0]][vert[1]])
        
