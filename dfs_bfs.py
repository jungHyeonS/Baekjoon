# from collections import deque

# grpah = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# def dfs(grpah,v,visited):
#     visited[v] = True
#     print(v,end = ' ')
#     for i in grpah[v]:
#         if not visited[i]:
#             dfs(grpah,i,visited)

# def bfs(grpah,start,visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in grpah[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# visited = [False] * 9
# bfs(grpah,1,visited)


# n,m = map(int,input().split())

# grpah = []
# for i in range(n):
#     grpah.append(list(map(int,input())))


# def dfs(x,y):

#     # 그래프 범위에서 벗어나면 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if grpah[x][y] == 0:
#         grpah[x][y] = 1
#         dfs(x - 1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 dfs 수행
#         if dfs(i,j) == True:
#             result += 1

# print(result)



n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

    
# print(graph)


for i in range(n):
    for j in range(m):
        print(graph[i][j])
