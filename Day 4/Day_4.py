f = open('Day_4_Input.txt', 'r')
lst = []
x = f.read().split('\n\n')
calledNum = x[0].split(',')
boards = []
rows = {}
colums = []
calledBoard = []
for row in range(1, len(x)):
    r  = x[row].split('\n')
    boards.append([])
    for num in r:
        boards[row - 1].append(num.split())
        rows[row - 1] = []
        for i in range(len(r)):
            rows[row - 1].append([])

calledBoard = boards
rowCount = 0
colCount = 0
for numCalled in calledNum:
    if rowCount == 5 or colCount ==5:
        break
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for num in range(len(boards[board][row])):
                if boards[board][row][num] == numCalled:
                    calledBoard[board][row][num] = 'called'

    ### check row ###
    for board in range(len(boards)):
        if rowCount == 5:
                break
        for row in range(len(boards[board])):
            if rowCount == 5:
                break
            rowCount = 0
            for num in range(len(boards[board][row])):
                if calledBoard[board][row][num] == 'called':
                    rowCount +=1
                    if rowCount > 4:
                        winner = board
                        lastNum = int(numCalled)
                        break
    ### check col
    for board in range(len(boards)):
        if colCount == 5:
                break
        for col in range(len(boards[board])):
            if colCount == 5:
                break
            colCount = 0
            for num in range(len(boards[board][row])):
                if calledBoard[board][num][col] == 'called':
                    colCount +=1
                    if colCount > 4:
                        winner = board
                        lastNum = int(numCalled)
                        break

sum = 0
for row in calledBoard[winner]:
    for num in row:
        if num != 'called':
            sum += int(num)
print(sum * lastNum)

''' part two'''
winnerBoards = []
calledNum = x[0].split(',')
boards = []
rows = {}
colums = []
calledBoard = []
for row in range(1, len(x)):
    r  = x[row].split('\n')

    boards.append([])
    for num in r:
        boards[row - 1].append(num.split())
        rows[row - 1] = []
        for i in range(len(r)):
            rows[row - 1].append([])

calledBoard = boards
rowCount = 0
colCount = 0
for numCalled in calledNum:
    if len(winnerBoards) == len(boards):
            break
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for num in range(len(boards[board][row])):
                if boards[board][row][num] == numCalled:
                    calledBoard[board][row][num] = 'called'
    ### check row ###
    for board in range(len(boards)):
        if len(winnerBoards) == len(boards):
            break
        for row in range(len(boards[board])):
            if len(winnerBoards) == len(boards):
                break
            rowCount = 0
            for num in range(len(boards[board][row])):
                if calledBoard[board][row][num] == 'called':
                    rowCount +=1
                    if rowCount > 4:
                        # winner = board
                        lastNum = int(numCalled)
                        if board not in winnerBoards:
                            winnerBoards.append(board)
                        if len(winnerBoards) == len(boards):
                            winner = board
                            break
                       
            
    ### check col
    for board in range(len(boards)):
        if len(winnerBoards) == len(boards):
            break
        for col in range(len(boards[board])):
            if len(winnerBoards) == len(boards):
                break
            colCount = 0
            for num in range(len(boards[board][row])):
                if calledBoard[board][num][col] == 'called':
                    colCount +=1
                    if colCount > 4:
                        lastNum = int(numCalled)
                        if board not in winnerBoards:
                            winnerBoards.append(board)
                        if len(winnerBoards) == len(boards):
                            winner = board
                            break
                       

sum = 0
for row in calledBoard[winner]:
    for num in row:
        if num != 'called':
            sum += int(num)
print(sum * lastNum)
