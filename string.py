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


import sys
chd = sys.stdin.readline().strip()
print(len(chd.split()))