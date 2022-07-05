from collections import deque

#n,m 입력
n,m = map(int, input().split())


# 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int,input())))



# 이동할 네 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(x,y):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque()

    # 초기 큐 추가(0,0)
    queue.append((x,y))

    # 큐가 빌때 까지 반복
    while queue:
        # 현재 위치에 큐 하나 빼기
        x,y = queue.popleft()

        # 현재 위치 기준 네 방향으로 위치 확인
        for i in range(4):
            # 이동 거리 구하기
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵의 영역을 벗어났을 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 이동할 공간이 벽인 경우
            if graph[nx][ny] == 0:
                continue
            
            # 이동할 공간이 벽이 아닌 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))