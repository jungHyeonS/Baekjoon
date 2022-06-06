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


import sys
num1 = int(sys.stdin.readline())
for i in range(0,num1):
    chd = sys.stdin.readline().strip().split(" ")
    for j in range(0,len(chd[1])):
        print(chd[1][j] * int(chd[0]),end="")
    print("")
        




