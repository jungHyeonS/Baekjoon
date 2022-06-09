# print(ord(input()))

# import sys
# num1 = int(sys.stdin.readline())
# chd = sys.stdin.readline().strip()
# sum = 0
# for i in list(chd):
#     sum = sum + int(i)

# print(sum)


# import sys
# chd = sys.stdin.readline().strip()
# aplah = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in range(0,len(aplah)):
#     for j in range(0,len(chd)):
#         a = -1
#         if aplah[i] == chd[j]:
#             a = j
#             break
#     print(a,end=" ")


# import sys
# num1 = int(sys.stdin.readline())
# for i in range(0,num1):
#     chd = sys.stdin.readline().strip().split(" ")
#     for j in range(0,len(chd[1])):
#         print(chd[1][j] * int(chd[0]),end="")
#     print("")
        



# import sys
# chd = sys.stdin.readline().strip().lower()
# subchd = ''.join(dict.fromkeys(chd))
# res = []
# for i in range(0,len(subchd)):
#     res.append(chd.count(subchd[i]))

# resub = sorted(res,reverse=True)
# if len(resub) > 1 and resub[0] == resub[1]:
#     print("?")
# else:
#     tmp = max(res)
#     index = res.index(tmp)
#     print(subchd[index].upper())


# import sys
# chd = sys.stdin.readline().strip()
# print(len(chd.split()))

# chd1,chd2 = input().split()

# if int(chd1[::-1]) > int(chd2[::-1]):
#     print(chd1[::-1])
# else:
#     print(chd2[::-1])


# str = ['','','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# import sys
# chd = sys.stdin.readline().strip()
# time = 0

# for i in chd:
#     for j in range(0,len(str)):
#         if i in str[j]:
#             time = time + j

# print(time)


import sys
chd = sys.stdin.readline().strip()

str = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
for i in range(len(chd) - 1):
    x = chd[i] + chd[i + 1]
    if x == 'dz' and chd[i + 2] == '=':
        x = chd[i] + chd[i + 1] + chd[i + 2]
    print(x)
    # for j in str:
    #     if x == j:
    #         count = count + 1

print(count)