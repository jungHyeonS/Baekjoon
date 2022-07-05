# from collections import deque
# # L 마다 최대 거리 구하기

# n,m = map(int,input().split())
# graph = [list(map(str, input())) for _ in range(n)]
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(x,y):
#     queue = deque()
#     queue.append([x,y])
#     subGrpah = [[0]*m for _ in range(n)]
#     subGrpah[x][y] = 1
#     cnt = 0
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 'L' and subGrpah[nx][ny] == 0:
#                     subGrpah[nx][ny] = subGrpah[x][y] + 1
#                     cnt = max(cnt,subGrpah[nx][ny])
#                     queue.append([nx,ny])
#     return cnt - 1
# maxCnt = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'L':
#             maxCnt = max(maxCnt,bfs(i,j))
# print(maxCnt)


# --정답

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

# BFS 함수 
def bfs(x,y,cnt):
    # 한 지점에서 bfs를 돌 때 현재 cnt값이 최대인지 아닌지를 구분하기 위해 
    # max_를 갱신해준다.
    max_ = -1
    q = deque()
    q.append((x,y,cnt))
    visited[x][y] = 1
    while q:
        x,y,cur_cnt = q.popleft()
        # max_를 갱신해준다.
        if max_ < cur_cnt:
            max_ = cur_cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<=ny<m and graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                # 여기서 현재 좌표의 cnt에서 다음 좌표로 넘어갈 때 cnt + 1 을 해준다.
                q.append((nx,ny,cur_cnt+1))
                visited[nx][ny] = 1
    # 갱신해줬던 max_ 값을 return 해준다/
    return max_

# Max변수 선언
Max = -1
for i in range(n):
    for j in range(m):
        # L 일 때만 bfs함수를 실행시켜줘야 한다.  이부분을 놓쳐서 허무하게 시간을 날렸다..
        if graph[i][j] == 'L':
            visited = [[0] * (m) for _ in range(n)]
            Max = max(Max,bfs(i,j,0))
print(Max)

# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW

# 0, 0, 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0, 0, 0
# 1, 0, 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0, 0, 0

# 'W', 5, 7, 'W', 'W', 'W', 'L'
# 2, 4, 6, 'W', 'L', 'L', 'L'
# 1, 'W', 8, 'W', 'L', 'W', 'W'
# 3, 'W', 9, 'W', 'L', 'L', 'L'
# 'W', 11, 10, 'W', 'L', 'W', 'W'


# 'W', 4, 6, 'W', 'W', 'W', 'L'
# 2, 3, 5, 'W', 'L', 'L', 'L'
# 1, 'W', 7, 'W', 'L', 'W', 'W'
# 0, 'W', 8, 'W', 'L', 'L', 'L'
# 'W', 10, 9, 'W', 'L', 'W', 'W'


# 'W', 5, 6, 'W', 'W', 'W', 'L'
# 2, 3, 4, 'W', 'L', 'L', 'L'
# 1, 'W', 7, 'W', 'L', 'W', 'W'
# 0, 'W', 8, 'W', 'L', 'L', 'L'
# 'W', 10, 9, 'W', 'L', 'W', 'W'