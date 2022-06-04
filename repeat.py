
# num1 = int(input())
# for i in range(1,10):
#     print(str(num1) + str(" * ") + str(i) + str(" = ") + str((num1 * i)))


# num1 = int(input())
# for i in range(1,(num1+1)):
#     num2,num3 = map(int,input().split())
#     print(num2 + num3)

# num1 = int(input())
# sum = 0
# for i in range(1,(num1+1)):
#     sum += i
# print(sum)

# import sys
# num1 = int(sys.stdin.readline())
# for i in range(1,(num1+1)):
#     num2,num3 = map(int,sys.stdin.readline().split())
#     print(num2 + num3)

# import sys
# num1 = int(sys.stdin.readline())
# for i in range(1,(num1+1)):
#     print(i)

# import sys
# num1 = int(sys.stdin.readline())
# for i in range(num1,0,-1):
#     print(i)

# import sys
# num1 = int(sys.stdin.readline())
# for i in range(1,(num1+1)):
#     num2,num3 = map(int,sys.stdin.readline().split())
#     print(str("Case #")+str(i)+str(": ") +str(num2) + str(" + ") +str(num3)+str(" = ") + str((num2 + num3)))


# import sys
# num1 = int(sys.stdin.readline())
# for i in range(1,(num1+1)):
#     for j in range(1,(i+1)):
#         print("*",end="")
#     print("")



# import sys
# num1 = int(sys.stdin.readline())
# for i in range(1,(num1+1)):
#     print(" "*(num1 - i) + "*" * i)

# import sys
# n,x = map(int,sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# for i in arr:
#     if i < x:
#         print(i,end=" ")

# import sys
# while True:
#     try:
#         num1,num2 = map(int,sys.stdin.readline().split())
#         sum = num1 + num2
#         print(sum)
#     except:
#         break

import sys
import math
num1 = int(sys.stdin.readline())
a = 0
b = 0
ab = 0
c = num1
count = 0

while True:
    if c < 10:
        a = 0
    else:
        a = math.trunc(c / 10)
    b = math.trunc(c % 10)
    ab = a + b

    if ab > 9:
       ab = math.trunc(ab % 10)
    c = int(str(b) + str(ab))
    count = count + 1
    if c == num1:
        break

print(count)

# while True:
# a = math.trunc(num1 / 10)
# b = math.trunc(num1 % 10)
# c = a + b
# temp = int(str(b) + str(c))
# if temp == num1:
#     break
# print(int(str(b) + str(c)))
# print(math.trunc(a))
# print(math.trunc(b))
    