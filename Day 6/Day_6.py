from collections import defaultdict
f = open('Day_6_Input.txt', 'r')
x = f.read().split(',')
for i in range(80):
    for index in range(len(x)):
        num = int(x[index]) - 1
        if num < 0:
            x.append(8)
            num = 6
        x[index] = num
print(len(x))
'''part two, part one would take forever so i had to rewrite it. learned default dict is pretty cool and doesnt create and error if a key doesnt exist since it just creates it'''

numbers = defaultdict(int)
for i in range(len(x)):
    numbers[int(x[i])] += 1
for i in range(256):
    new = defaultdict(int)
    for k,v in numbers.items():
        if k > 0:
            new[k - 1] += v
        else:
            new[8] += v
            new[6] += v
    numbers = new
total = 0
for k,v in numbers.items():
    total += v

print(total)

