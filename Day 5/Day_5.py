f = open('Day_5_Input.txt', 'r')
x = f.read().split('\n')
calledCoor = {}
dups = 0
for points in x:
    coor = points.split('->')
    first = coor[0].strip()
    second = coor[1].strip()
    x1 = int(first.split(',')[0])
    y1 = int(first.split(',')[1])
    x2 = int(second.split(',')[0])
    y2 = int(second.split(',')[1])
 
    if x1 == x2:
        small = min(y1, y2)
        big = max(y1, y2)
        for i in range(small, big + 1):
            if (x1, i) not in calledCoor:
                calledCoor[x1, i] = 1
            else:
                calledCoor[x1, i] += 1

    elif y1 == y2:
        small = min(x1, x2)
        big = max(x1, x2)
        for i in range(small, big + 1):
            if (i, y1) not in calledCoor:
                calledCoor[i, y1] = 1
            else:
                calledCoor[i, y1] += 1

    else:
        diff = abs(x1 - x2)
        if x1 > x2:
            addx = -1
        else:
            addx = 1
        if y1 > y2:
            addy = -1
        else:
            addy = 1

        for i in range(diff + 1):
            if (x1 + (addx * i), y1 + (addy * i)) not in calledCoor:
                calledCoor[x1 + (addx * i), y1 + (addy * i)] = 1
            else:
                calledCoor[x1 + (addx * i), y1 + (addy * i)] += 1
for k,v in calledCoor.items():
    if v > 1:
        dups += 1
print(dups)

