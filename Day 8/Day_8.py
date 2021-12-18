f = open('Day_8_Input.txt', 'r')
x = f.read().split('\n')
info = []
data = []
for i in x:
    info.append(i.split('|'))

for i in info:
    data.append(i[1].split())


count = 0
for i in data:
    for entry in i:
        if len(entry) in [2, 3, 4, 7]:
            count += 1

print(count)
'''1, 4, 7 8'''
'''
0 - 6 good
1 - 2 good
2 - 5
3 - 5 
4 - 4 good
5 - 5
6 - 6 
7 - 3 good
8 - 7 good
9 - 6 

'''
'''part two, realized i could have used 7 to get 9 but whatev'''
info = []
data = []
usp = []
display = {}
for i in x:
    info.append(i.split('|'))

for i in info:
    usp.append(i[0].split())
    data.append(i[1].split())

index = 0
total = 0
for i in usp:
    display = {}
    for entry in i:
        if len(entry) == 2:
            display[1] = ''.join(sorted(entry))
        elif len(entry) == 3:
            display[7] = ''.join(sorted(entry))
        elif len(entry) == 4:
            display[4] = ''.join(sorted(entry))
        elif len(entry) == 7:
            display[8] = ''.join(sorted(entry))
    for entry in i:
        if len(entry) == 6:
            is9 = True
            is6 = True
            for letter in display[1]:
                if letter not in entry:
                    display[6] = ''.join(sorted(entry))
                    is9 = False
                    is6 = False
            if is6:
                for letter in display[4]:
                    if letter not in entry:
                        display[0] = ''.join(sorted(entry))
                        is9 = False
            if is9:
                display[9] = ''.join(sorted(entry))
        if len(entry) == 5:
            for letter in display[1]:
                is3 = False
                if letter not in entry:
                    nonMatch = 0
                    for l in display[4]:
                        if l not in entry:

                            nonMatch += 1
                    if nonMatch == 1:
                        display[5] = ''.join(sorted(entry))
                    else:
                        display[2] = ''.join(sorted(entry))
                    break
                is3 = True
            if is3:
                display[3] = ''.join(sorted(entry))
   
    flippedDisplay = {}
    for k,v in display.items():
        flippedDisplay[v] = k


    outputTotal = ''
    for value in data[index]:
        sortedString = ''.join(sorted(value))
        outputTotal += str(flippedDisplay[''.join(sorted(value))])
    total += int(outputTotal)
    
    index += 1
print(total)