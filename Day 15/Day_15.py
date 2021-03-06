from collections import defaultdict
f = open('Day_15_Input.txt', 'r')
grid = f.read().split('\n')
baseGrid = grid.copy()
newBases = []
blank = []

''' part two'''
def genGrid(baseGrid, newBases, first: bool):
    newGrid = baseGrid.copy()
    updatedGrid = baseGrid.copy()
    number = 0
    for index in range(4):
        changingGrid = []
        for row in range(len(newGrid)):
            updatedRow = ''
            for num in newGrid[row]:
                updatedNum = int(num) + 1
                if updatedNum > 9:
                    updatedNum = 1
                updatedRow += str(updatedNum)
        
            updatedGrid[row] += updatedRow
            changingGrid.append(updatedRow)
        if first:
            newBases.append(changingGrid)
        
        newGrid = changingGrid
    return updatedGrid


grid = genGrid(grid, newBases, True) 
for base in newBases:
    grid += genGrid(base, blank, False)   

''' end part two, comment out above to run part one'''

cavernWidth = len(grid[0])
cavernLength = len(grid)
vertDistances = {(0, 0): 0}
adjacentVerts = {(0, 0): []}
end = (cavernLength - 1, cavernWidth - 1)

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
totalRisk = 0
while True:
    adjacentVerts = findAdjacent(adjacentVerts)
    smallestVert = ''
    smallestRisk = 100000000000
    for k, v in adjacentVerts.items():
        keyDist = vertDistances[k]
        for vert in v:
            Y, X = vert[0], vert[1]
            risk = int(grid[Y][X])
            totalRisk = keyDist + risk
            if totalRisk < smallestRisk:
                smallestRisk = totalRisk
                smallestVert = (Y, X)
                lastVert = k

    vertDistances[smallestVert] = smallestRisk
    adjacentVerts[smallestVert] = []
    if smallestVert == end:
        break
print(vertDistances[(end)])

'''part two take a while but it works '''
