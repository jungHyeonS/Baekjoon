
import sys
# N,M,K = map(int,sys.stdin.readline().split())
# Narray = list(map(int, sys.stdin.readline().split()))

# Narray.sort(reverse=True)

# sum = 0


# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         sum += Narray[0]
#         M -= 1
#     if M == 0:
#         break
#     sum += Narray[1]
#     M -= 1

# print(sum)


# N,M = map(int,sys.stdin.readline().split())
# maxArr = []
# for i in range(N):
#     arr = w
#     maxArr.append(min(arr))

# print(max(maxArr))



N,K = map(int,sys.stdin.readline().split())

count = 0
while True:
    if N == 1:
        break
    
    if N % K == 0:
        N = N / K
    else:
        N -= N
    count += 1

print(count)