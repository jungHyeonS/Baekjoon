# 
# num1,num2 = input().split()

# print(int(num1) + int(num2))
# print(int(num1) - int(num2))
# print(int(num1) * int(num2))
# print(math.trunc(int(num1) / int(num2)))
# print(int(num1) % int(num2))


# text = input()
# print(text + "??!")

# year = input()
# print(int(year) - 543)

# num1,num2,num3 = input().split()
# a = int(num1)
# b = int(num2)
# c = int(num3)
# print((a+b)%c)
# print(((a%c) + (b%c))%c)
# print((a*b)%c)
# print(((a%c) * (b%c))%c)

# import math
# num1 = input()
# num2 = input()
# first = int(num2) % 10
# second = math.trunc((int(num2) / 10)) % 10
# thred = math.trunc(math.trunc((int(num2) / 10)) / 10)

# num3 = int(num1) * first
# num4 = str(int(num1) * second) + "0"
# num5 = str((int(num1) * thred)) + "00"
# print(num3)
# print(int(num1) * second)
# print((int(num1) * thred))
# print(num3 + int(num4) + int(num5))


# num1,num2 = input().split()
# a = int(num1)
# b = int(num2)
# if a < b:
#     print("<")
# elif a > b:
#     print(">")
# elif a == b:
#     print("==")

# num1 = input()
# score = int(num1)
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# year = int(input())
# if year % 4 == 0 and year % 100 != 0:
#     print("1")
# elif year % 400 == 0:
#     print("1")
# else:
#     print("0")


# num1 = int(input())
# num2 = int(input())

# if num1 > 0 and num2 > 0:
#     print("1")
# elif num1 < 0 and num2 > 0:
#     print("2")
# elif num1 < 0 and num2 < 0:
#     print("3")
# elif num1 > 0 and num2 < 0:
#     print("4")
    


# num1,num2 = input().split()
# hour = int(num1)
# min = int(num2)



# if min >= 45:
#     min = min-45
# else:
#     tempMin = 45-min
#     min = 60 - tempMin
#     hour = hour -1
#     if hour < 0:
#         hour = 23

# print(hour,min,sep=' ')

# import math
# num1,num2 = input().split()
# step = int(input())
# hour = int(num1)
# min = int(num2) + step


# if min >= 60:
#     hour = math.trunc(hour + (min / 60))
#     min = min % 60
#     if hour > 23:
#         hour = hour - 24

# print(hour,min,sep=' ')


num1,num2,num3 = map(int,input().split())


if (num1 == num2) and (num1 == num3) and (num2 == num3):
    print(10000 + (num1 * 1000))
elif (num1 != num2) and (num1 != num3) and (num2 != num3):
    max = 0
    if(num1 > num2 and num1 > num3):
        max = num1
    elif(num2 > num1 and num2 > num3):
        max = num2
    else:
        max = num3
    print(max * 100)
else:
    equls = 0
    if(num1 == num2 or num1 == num3):
        equls = num1
    elif(num2 == num1 or num2 == num3):
        equls = num2
    else:
        equls = num3
    print(1000 + (equls * 100))