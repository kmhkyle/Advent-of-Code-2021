f = open('Day_15_Input.txt', 'r')
grid = f.read().split('\n')

cavernWidth = len(grid[0])
cavernLength = len(grid)
print(cavernLength, cavernWidth)

def checkNorth(Y, X):
    return grid[Y - 1][X]



def findRisk(currentY, currentX, visitedDistance):
    #edge cases
    if currentY == 0:
        if currentX == 0:
            pass
        elif currentX == cavernWidth - 1:
            pass
        else:
            pass





    for y in range(cavernLength):
        for x in range(cavernWidth):
            print(grid[y][x])



print(checkNorth(1,2))
    