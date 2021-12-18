f = open('Day_11_Input.txt', 'r')
x = f.read().split('\n')
# making int a list with ints because i dont feel like casting int everytime #
grid = []
for line in x:
    numbers = [int(number) for number in line]
    grid.append(numbers)


NW, N, NE, E = [-1, -1], [-1, 0], [-1, 1], [0, 1]
SE, S, SW, W = [1, 1], [1, 0], [1, -1], [0, -1]



def flash(row, column):
    grid[row][column] = 'flashed'
    if row == 0:
        if column == 0:
            for r,c in [E, SE, S]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
            #dont do top or left
        elif column == len(grid[0]) - 1:
            for r,c in [W, SW, S]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
            #doont do top or right
        else:
            for r,c in [W, SW, S, SE, E]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
            #dont do top
    elif row == len(grid) - 1:
        if column == 0:
            for r,c in [N, NE, E]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
            #dont do bottom or left
        elif column == len(grid[0]) - 1:
            for r,c in [N, NW, W]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
            # dont do bottom or right
        else:
            for r,c in [N, NW, W, NE, E]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
            #dont do bottom
    elif column == 0:
        for r,c in [N, NE, E, S, SE]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
        #dont do left
    elif column == len(grid[0]) - 1:
        for r,c in [N, NW, W, S, SW]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
        #dont do right
    else:
        for r,c in [N, NW, W, SW, S, SE, E, NE]:
                if grid[row + r][column + c] != 'flashed':
                    grid[row + r][column + c] += 1
        #do all 
numFlashes = 0
for i in range(2000):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
    while True:
        currentFlashes = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] != 'flashed' and grid[row][column] > 9:
                    numFlashes += 1
                    currentFlashes += 1
                    flash(row,column)
        if currentFlashes == 0:
            break
    
    total = 0
    for rr in range(len(grid)):
        for cc in range(len(grid[r])):
            if grid[rr][cc] == 'flashed':
                grid[rr][cc] = 0
        total += sum(grid[rr])
    if total == 0:
        #im a moron so it took me 5 min to realize that you need to add 1 to the index since step 1 == index 0
        print(i + 1)
        break


print(numFlashes)