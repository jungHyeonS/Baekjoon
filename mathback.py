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



# num1 = int(input())

# 1 = 1/1
# 2 = 1/2


numerator = 0
denominator = 0
ischange = 0
for i in range(1,3):
    for j in range(1,(i+1)):
        if ischange == 0:
            numerator = j
            denominator = j
            ischange = 1
        elif ischange == 1:
            numerator = j
            denominator = i
            # numerator = numerator + 1
            # denominator = denominator - 1
        print(str(numerator) + "/" + str(denominator))


