import sys
num1,num2,num3 = map(int,sys.stdin.readline().split())

if num2 >= num3:
    print("-1")
else:
    print(int(num1 / (num3 - num2)+1))
