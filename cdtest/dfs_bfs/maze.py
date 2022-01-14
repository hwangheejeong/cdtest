#미로탈출
#괴물이 있으면 > 0
#괴물이 없으면 > 1
#한번에 한칸씩 최소 이동 거리 => BFS
from collections import deque

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

#상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        #큐의 맨 위의 값
        x,y = queue.popleft()

        #상하좌우 방문
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #범위가 아닐 경우
            if nx>=N or nx<0 or ny<0 or ny>=M:
                continue
            #괴물이 있을 경우(벽인 경우)
            if graph[nx][ny] == 0:
                continue
            #방문
            if graph[nx][ny] == 1:
                graph[nx][ny]=graph[x][y]+1
                #큐에 넣어주기
                queue.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0,0))