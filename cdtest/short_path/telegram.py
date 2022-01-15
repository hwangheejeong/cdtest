#전보
#다익스트라 알고리즘
#최단거리

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(c):
    q = []
    # 시작노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        # 가장 최단거리의 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리했다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count_city=0
max_dist =0

for d in distance:
    if d != INF:
        count_city+=1
        max_dist=max(d,max_dist)

print(count_city-1,max_dist)