import statistics
f = open('Day_7_Input.txt', 'r')
x = f.read().split(',')
info = [int(i) for i in x]



num = statistics.median(info)

total = 0
for i in x:
    total += abs(int(i) - num)
print(total)
'''part 2'''

small = min(info)
big = max(info)

minFuel = 9999999999
for i in range(small, big + 1):
    fuelUse = 0
    for c in info:
        distance = abs(c - i)
        fuelUse += ((distance * (distance+ 1)) / 2)
    if minFuel > fuelUse:
        minFuel = fuelUse

print(minFuel)


# instructions = open('Day_7_Input.txt').read().split(",")

# crabs = [int(i) for i in instructions]
# min_position = min(crabs)
# max_position = max(crabs)

# min_fuel_use = math.inf
# for i in range(min_position, max_position + 1):
#   fuel_use = 0
#   for crab in crabs:
#     distance = abs(crab - i)
#     fuel_use += ((distance**2 + distance)/2)
#   if min_fuel_use > fuel_use:
#     min_fuel_use = fuel_use

# print(min_fuel_use)