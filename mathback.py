# import sys
# num1,num2,num3 = map(int,sys.stdin.readline().split())

# if num2 >= num3:
#     print("-1")
# else:
#     print(int(num1 / (num3 - num2)+1))


# 벌집
# num1 = int(input())

# polygon = 1
# cnt = 1
# while num1 > polygon:
#     polygon += 6 * cnt
#     cnt = cnt + 1

# print(cnt)
# 1
# 2,3,4,5,6,7
# 8,9,10,11,12,13,14,15,16,17,18,19




# 1 = 1/1
# 2 = 1/2

# num1 = int(input())
# numerator = 0
# denominator = 0
# ischange = True
# count = 1
# for i in range(1,num1):
#     temp = i
#     for j in range(1,(i+1)):
#         if i % 2 == 0:
#             numerator = j
#             denominator = temp
#         else:
#             numerator = temp
#             denominator = j

#         temp = temp-1
#         if count == num1:
#             ischange = False
#             break
#         count = count+1
#     if ischange == False:
#         break



# num1 = int(input())
# line = 1
# while num1 > line:
#     num1 = num1 - line
#     line = line + 1

#     if line % 2 == 0:
#         numerator = 
# print(str(numerator) + "/" + str(denominator))

# n = int(input())

# line = 0
# end = 0
# while n > end:
#     line += 1
#     end += line


# diff = end - n
# if line%2 == 0: #짝수 라인 일때
#     top = line - diff
#     bottom = diff + 1
# else:
#     top = diff + 1
#     bottom = line - diff

# print(str(top) + "/" + str(bottom))


# print(6/5)


        # if ischange == 0:
        #     numerator = j
        #     denominator = j
        #     ischange = 1
        # elif ischange == 1:
        #     numerator = j
        #     denominator = i
            # numerator = numerator + 1
            # denominator = denominator - 1
        # print(str(numerator) + "/" + str(denominator))



import sys
A,B,V = map(int,sys.stdin.readline().split())


# print(V-(A-B))


# 0 5 1 = 4
# 4 5 6 = 9 3


# v - a = 1

# 5 / 4
import math

print(math.ceil(V / (A-B)))

# print(1000000000 - 99)
# print(B-A)

# temp = 0
# count = 0
# while True:
#     temp += A - B
#     if temp == V:
#         break
#     count = count + 1

# print(count)