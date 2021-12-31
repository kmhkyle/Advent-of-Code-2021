from collections import defaultdict
f = open('Day_17_Input.txt', 'r')
data = f.read().split()
xRaw = data[2].strip(',').split('=')[1].split('..')
yRaw = data[3].split('=')[1].split('..')
x = range(int(xRaw[0]), int(xRaw[1]) + 1)
y = range(int(yRaw[0]), int(yRaw[1]) + 1)

xCounts = defaultdict(list)
infinteXs = []
def xPos(startingX, range, pos, infinites):
    count = 1
    sumX = startingX
    start = startingX
    while sumX <= max(range):
        if sumX >= min(range):
            pos[count].append(start)
        count += 1
        startingX -= 1
        if startingX < 1:
            if sumX > min(range) and sumX < max(range):
                infinteXs.append(start)
            break
        sumX += startingX
    return pos

for i in range(max(x) + 1):
    xPos(i, x, xCounts, infinteXs)

def yPos(startingY, minY, positions):
    count = 1
    position = startingY
    start = startingY
    while position >= minY:
        if position in y:
            positions[count].append(start)
        startingY -= 1
        position += startingY
        count += 1
    return positions
yCounts = defaultdict(list)

for i in range(min(y), abs(min(y))):
    yPos(i, min(y), yCounts)

nums = []
for i in range(max(yCounts.keys()) + 1):
    if len(xCounts[i]) < len(infinteXs):
        xCounts[i] = infinteXs
for k, v in yCounts.items():
    for v2 in xCounts[k]:
        for i in v:
            if [v2, i] not in nums:
                nums.append([v2, i])

maxY = 0
for i in nums:
    if i[1] > maxY:
        maxY = i[1]
highestY = (maxY ** 2 + maxY) / 2
print(int(highestY))
print(len(nums))
