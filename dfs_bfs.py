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
# dfs(grpah,1,visited)


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



# n,m = map(int,input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

    
# # print(graph)


# for i in range(n):
#     for j in range(m):
#         print(graph[i][j])






# 음료수 얼려먹기
# 입력간이 0인것만 방문
# 0인거를 방문했으면 1로 변경


n,m = map(int,input().split())

# 2차원 리스트로 맵정보 입력
grpah = []
for i in range(n):
    grpah.append(list(map(int,input())))


# 특정 노드를 방문후에 그 노드와 연결되어있는(0) 을 모두 방문
def dfs(x,y):

    # 범위를 벗어난경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #현재 노드를 방문하지 않았을경우
    if grpah[x][y] == 0:
        # 해당 노드를 방문 처리
        grpah[x][y] = 1

        # 해당 노드를 기준으로 상,하,좌,우 노드를 방문
        dfs(x - 1,y)
        dfs(x,y-1)
        dfs(x + 1,y)
        dfs(x,y+1)
        
        # 여기가 중요 0,0 
        # 00110
        # 00011
        # 11111
        # 00000
        # 해당 맵 기준으로 0,0 부터 방문하여 연결되어있는 모든 0의 노드를을 연결처리 시키면
        # 아래 반복문에서 묶음처리가 되어 3개가 생김
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)