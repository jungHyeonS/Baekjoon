# import sys
# num1 = int(sys.stdin.readline())
# numList = list(map(int, sys.stdin.readline().split()))
# max = numList[0]
# min = numList[0]
# for i in numList:
#     if max <= i:
#        max = i
#     if min >= i:
#        min = i
# print(min,max,end=" ")

# import sys
# max = 0
# count = 0
# for i in range(1,10):
#     num1 = int(sys.stdin.readline())
#     if max <= num1:
#         max = num1
#         count = i

# print(max)
# print(count)

# import sys
# A = int(sys.stdin.readline())
# B = int(sys.stdin.readline())
# C = int(sys.stdin.readline())

# num = A * B * C
# numList = list(map(int, str(num)))
# result = [0,0,0,0,0,0,0,0,0,0]
# for i in range(0,10):
#     for j in numList:
#         if i == j:
#             result[i] += 1
#     print(result[i])

# import sys
# result = []
# for i in range(0,10):
#     num1 = int(sys.stdin.readline())
#     result.append(num1 % 42)

# s = set(result)
# print(len(s))

# import sys
# num1 = int(sys.stdin.readline())
# score = list(map(int, sys.stdin.readline().split()))
# m = 0
# sum = 0
# avg = 0
# for i in score:
#     if m < i:
#         m = i

# for j in score:
#     j = j/m * 100
#     sum = sum + j


# avg = sum / num1
# print(avg)

# import sys
# num1 = int(sys.stdin.readline())
# for i in range(num1):
#     # print(i)
#     word = sys.stdin.readline()
#     lst = []
#     lst.extend(word)
#     sum = 0
#     count = 0
#     for j in lst:
#         if j == "O":
#             count = count + 1
#         else:
#             count = 0
#         sum = sum + count
#     print(sum)


import sys
num1 = int(sys.stdin.readline())
for i in range(num1):
    lst = list(map(int, sys.stdin.readline().split()))
    num = lst.pop(0)
    sum = 0
    avg = 0
    for j in lst:
        sum = sum + j
    avg = sum / num
    count = 0
    for j in lst:
        if j > avg:
            count = count + 1
    score = round((count / num) * 100.0,3)
    print("{:.3f}%".format(score))
    