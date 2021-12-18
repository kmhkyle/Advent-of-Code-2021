f = open('Day_13_Input.txt', 'r')
x = f.read().split('\n\n')
rawInstructions = x[0].split('\n')
rawFolds = x[1].split('\n')



grid = []
folds = []
uniques = []
maxX = 0
maxY = 0
for i in rawInstructions:
    coor = i.split(',')
    grid.append([int(coor[0]), int(coor[1])])
for i in rawFolds:
    fold = i.split('=')
    folds.append([fold[0][-1], int(fold[1])])
currentX = folds[0][1] * 2
currentY = folds[1][1] * 2


def foldPaper(direction,  lines):
    if direction == 'y':
        for instr in range(len(grid)):
            if grid[instr][1] > lines:
                diff = grid[instr][1] - lines
                grid[instr][1] -= diff * 2
    elif direction == 'x':
        for instr in range(len(grid)):
            if grid[instr][0] > lines:
                diff = grid[instr][0] - lines
                grid[instr][0] -= diff * 2

for i in grid:
    if i not in uniques:
        uniques.append(i)

# part 1
# foldPaper('x', 655)
# print(len(uniques))
# part 2
for i in folds:
    foldPaper(i[0], i[1])


maxX, maxY = 0, 0
for x,y in uniques:
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y


screen = ""
for y in range(maxY + 1):
    for x in range(maxX + 1):
        if [x, y] in uniques:
            screen += '#'
        else:
            screen += ' '
    print(screen)
    screen = ''




