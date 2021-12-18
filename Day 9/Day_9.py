f = open('Day_9_Input.txt', 'r')
x = f.read().split('\n')

def checkRight(row, column):
    return int(x[row][column]) < int(x[row][column + 1])

def checkLeft(row, column):
    return int(x[row][column]) < int(x[row][column - 1])

def checkTop(row, column):
    return int(x[row][column]) < int(x[row -1][column])

def checkBottom(row, column):
    return int(x[row][column]) < int(x[row + 1][column])

lowPoints = []
lowPointsCoor = []
for row in range(len(x)):
    for number in range(len(x[row])):
        if row == 0:
            if number == 0:
                if checkRight(row, number) and checkBottom(row, number):
                    lowPoints.append(int(x[row][number]) + 1)
                    lowPointsCoor.append([row, number])
            elif number == len(x[row]) - 1:
                if checkLeft(row, number) and checkBottom(row, number):
                    lowPoints.append(int(x[row][number]) + 1)
                    lowPointsCoor.append([row, number])
            else:
                if checkLeft(row, number) and checkRight(row, number) and checkBottom(row, number):
                    lowPoints.append(int(x[row][number]) + 1)
                    lowPointsCoor.append([row, number])
        elif row == len(x) - 1:
            if number == 0:
                if checkTop(row, number) and checkRight(row, number):
                    lowPoints.append(int(x[row][number]) + 1)
                    lowPointsCoor.append([row, number])
            elif number == len(x[row]) - 1:
                if checkLeft(row, number) and checkTop(row, number):
                    lowPoints.append(int(x[row][number]) + 1)
                    lowPointsCoor.append([row, number])
            else:
                if checkLeft(row, number) and checkRight(row, number) and checkTop(row, number):
                    lowPoints.append(int(x[row][number]) + 1)
                    lowPointsCoor.append([row, number])
        elif number == 0:
            if checkTop(row, number) and checkRight(row, number) and checkBottom(row, number):
                lowPoints.append(int(x[row][number]) + 1)
                lowPointsCoor.append([row, number])
        elif number == len(x[row]) - 1:
            if checkTop(row, number) and checkLeft(row, number) and checkBottom(row, number):
                lowPoints.append(int(x[row][number]) + 1)
                lowPointsCoor.append([row, number])
        else:
            if checkTop(row, number) and checkRight(row, number) and checkLeft(row, number) and checkBottom(row, number):
                lowPoints.append(int(x[row][number]) + 1)
                lowPointsCoor.append([row, number])

print(sum(lowPoints))

length = len(x[0]) + 2
dataBorders = ['9' * length]
for i in x:
    dataBorders.append('9' + i + '9')
dataBorders.append('9' * length)
updatedCoor = []
updatedCoor = [[i[0]+1 , i[1]+ 1] for i in lowPointsCoor]

#now start checking#

totes = 0
count = 0
basinSizes = []
for i in updatedCoor:
    coor = [i[0], i[1]]
    basins = [coor]
    basinsToCheck = [coor]
    newBasinsToCheck = []
    while len(basinsToCheck) > 0:
        newBasinsToCheck = []
        for b in basinsToCheck:
            row = b[0]
            column = b[1]
            top = dataBorders[row - 1][column]
            topCoor = [row - 1, column]
            bottom = dataBorders[row + 1][column]
            bottomCoor = [row + 1, column]
            left = dataBorders[row][column - 1]
            leftCoor = [row, column - 1]
            right = dataBorders[row][column + 1]
            rightCoor = [row, column + 1]
            if top != '9' and topCoor not in basinsToCheck and topCoor not in newBasinsToCheck and topCoor not in basins:
                newBasinsToCheck.append(topCoor)
                basins.append(topCoor)
            if bottom != '9' and bottomCoor not in basinsToCheck and bottomCoor not in newBasinsToCheck and bottomCoor not in basins:
                newBasinsToCheck.append(bottomCoor)
                basins.append(bottomCoor)
            if left != '9' and leftCoor not in basinsToCheck and leftCoor not in newBasinsToCheck and leftCoor not in basins:
                newBasinsToCheck.append(leftCoor)
                basins.append(leftCoor)
            if right != '9' and rightCoor not in basinsToCheck and rightCoor not in newBasinsToCheck and rightCoor not in basins:
                newBasinsToCheck.append(rightCoor)
                basins.append(rightCoor)
            
            basinsToCheck = newBasinsToCheck
    basinSizes.append(len(basins))
basinSizes.sort()
print(basinSizes[-1] * basinSizes[-2] * basinSizes[-3])
