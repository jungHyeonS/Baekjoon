# def solve(a:list):
#     sum = 0
#     for i in a:
#         sum = sum + i
#     return sum

# solve([1,2,3,4,5])


# numbers = set(range(1, 10000))
# remove_set = set()
# for num in numbers :
#     for n in str(num):
#         num += int(n)
#     remove_set.add(num)

# self_numbers = numbers - remove_set 
# for self_num in sorted(self_numbers):
#     print(self_num)


# print(1-0)


def sequence(n):
    count = 0
    for i in range(1,(n+1)):
        if 100 > i:
            count = count + 1
        else:
            x = [int(a) for a in str(i)]
            des = None
            for index,value in enumerate(x):
                if index < (len(x)-1):
                    if des is None:
                        des = x[index] - x[index+1]
                    else:
                        newDes = x[index] - x[index+1]
                        if(des == newDes):
                            count = count + 1
                        else:
                            break
    print(count)


import sys
num1 = int(sys.stdin.readline())
sequence(num1)

# 1 2 3
# print(1-0)
# print(0-2)
# print(101 % 100)