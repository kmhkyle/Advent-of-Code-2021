f = open('Day_1_Input.txt', 'r')
lst = []
for line in f:
    lst.append(int(line))
# lst = f.read().split('\n')
f.close()

def partOne():
    first = lst[0]
    count = 0
    for number in range(1, len(lst)):
        second = lst[number]
        if second > first:
            count += 1
        first = second
    return count

def partTwo():
    first = lst[0] + lst[1] + lst [2]
    count = 0
    for i in range(1, len(lst) - 2):
        second = lst[i] + lst[i + 1] + lst[i + 2]
        if second > first:
            count += 1
        first = second
    return count

print(partOne(), partTwo())