f = open('Day_3_Input.txt', 'r')
lst = []
for line in f:
    lst.append((line.strip('\n')))
# lst = f.read().split('\n')
f.close()
# one = 0
# zero  = 0
# gamma = ''
# ep = ''
# # print(lst)
# for letter in range(len(lst[0])):
#     one = 0
#     zero  = 0
#     for num in range(len(lst)):
#         if lst[num][letter] == '0':
#             zero += 1
#         else:
#             one += 1
#     if one > zero:
#         gamma += '1'
#         ep += '0'
#     elif one == zero:
#         gamma += '1'
#         ep += '0'
#     elif one < zero:
#         gamma += '0'
#         ep += '1'
    # print(letter, zero, one)
# print(int(gamma, 2) * int(ep, 2))



# # one = 0
# # zero  = 0
# # gamma = ''
# # ep = ''
# # updatedLst = []
# # print(lst)
# # for letter in range(len(lst[0])):
# #     one = 0
# #     zero  = 0
# #     for num in range(len(lst)):
# #         if lst[num][letter] == '1':
# #             if 
# #             updatedLst.append(lst[num])

# #         else:
# #             one += 1
# #     if one > zero:
# #         gamma += '1'
# #         ep += '0'
# #     else:
# #         gamma += '0'
# #         ep += '1'
#     # print(letter, zero, one)
# # for letter in range(len(lst)):
# #     # for letter in gamma:
# #     for letter in range(len(lst[0])):
# #         for num in range(len(lst)):
            

# #     # if lst[letter][0] == 1:
# #         if lst[letter][1] == 0:

# print(gamma)
# # print(gamma[2])
# for i in range(len(lst)):
#     # print(type(i))
#     answer = True
#     for letter in range(len(lst[i])):
#         if (lst[i][letter]) == gamma[letter]:
#           continue
#         else:
#             answer = False
#             break
#     if answer:
#         print(lst[i])
#         #     pass

#         #     break
#         # # else:
#         # #     break
#         # print(i) 
# while True:
new = lst
co2 = lst
# print(new)
for letter in range(len(new[0])):
    one = 0
    list1 = []
    list0 = []
    l0 = []
    l1 = []
    zero  = 0
    o = 0
    z = 0
    for num in range(len(new)):
        if new[num][letter] == '0':
            zero += 1
            list0.append(new[num])
        else:
            one += 1
            list1.append(new[num])
    if one > zero:
        new = list1
    elif one == zero:
        new = list1
    elif one < zero:
        new = list0
    
    if len(co2) > 1:
        for num in range(len(co2)):
            if co2[num][letter] == '0':
                z += 1
                l0.append(co2[num])
            else:
                o += 1
                l1.append(co2[num])
        if o > z:
            co2 = l0
        elif o == z:
            co2 = l0
        elif o < z:
            co2 = l1
    # print(co2,'\n' )


        
print(new, co2)
print(int(new[0], 2) *  int(co2[0], 2))

# from collections import Counter

# ll = [x for x in open('Day_3_Input.txt').read().strip().split('\n')]

# theta = ''
# epsilon = ''
# for i in range(len(ll[0])):
#     common = Counter([x[i] for x in ll])

#     if common['0'] > common['1']:
#         ll = [x for x in ll if x[i] == '0']
#     else:
#         ll = [x for x in ll if x[i] == '1']
#     theta = ll[0]

# ll = [x for x in open('Day_3_Input.txt').read().strip().split('\n')]
# for i in range(len(ll[0])):
#     common = Counter([x[i] for x in ll])

#     if common['0'] > common['1']:
#         ll = [x for x in ll if x[i] == '1']
#     else:
#         ll = [x for x in ll if x[i] == '0']
#     if ll:
#         epsilon = ll[0]
# print(int(theta,2)*int(epsilon,2))
# print(theta, epsilon)