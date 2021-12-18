f = open('Day_2_Input.txt', 'r')
lst = []
for line in f:
    lst.append((line))
# lst = f.read().split('\n')
f.close()
x = 0
y = 0
for i in lst:
    data = i.split()
    direction = data[0]
    amount = int(data[1])
    
    if direction == 'up':
        y += amount
    elif direction == 'down':
        y -= amount
    elif direction == 'forward':
        x += amount
print(abs(x) * abs(y))

aim = 0
depth = 0
hor = 0
for i in lst:
    data = i.split()
    direction = data[0]
    amount = int(data[1])
    if direction == 'up':
        aim -= amount
    elif direction == 'down':
        aim += amount
    elif direction == 'forward':
        depth += aim * amount
        hor += amount
    
print(depth * hor)
