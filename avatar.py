# import sys
# N = int(sys.stdin.readline())
# traval = 4 (map(str,sys.stdin.readline().split()))

# x = 1
# y = 1

# for item in traval:
#     if y == 1 and item == 'L':
#         continue
#     if y == N and item == 'R':
#         continue
#     if x == 1 and item == 'U':
#         continue
#     if x == N and item == 'D':
#         continue


#     if item == 'R':
#         y += 1
#     if item == 'L':
#         y -= 1
#     if item == 'U':
#         x -= 1
#     if item == 'D':
#         x += 1

# print(x,y,end=" ")

# import sys
# N = int(sys.stdin.readline())
# count = 0
# for i in range(N+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1


# print(count)


# inputData = input()
# row = int(inputData[1])
# column = int(ord(inputData[0])) - int(ord('a')) + 1

# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# result = 0
# for step in steps:
#     next_row = row + step[0]
#     newt_coloum = column + step[1]
#     if next_row >= 1 and next_row <= 8 and newt_coloum >= 1 and newt_coloum <= 8:
#         result += 1

# print(result)

import sys

N,M = map(int,sys.stdin.readline().split())
startRow,startColum,location = map(int,sys.stdin.readline().split())
mapAr = []
for i in range(N):
    mapAr.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,0]

while True:
    if mapAr[startRow - 1][startColum] == 1 and mapAr[startRow][startColum-1] == 1 and mapAr[startRow+1][startColum] == 1 and mapAr[startRow][startColum + 1] == 1:
        break
    
    if location == 3:
        location = 0
    else:
        location += 1
    

    


