#개선된 다익스트라
#시간복잡도 => 최악의 경우 O(ElogV)
#E는 간선의 개수
#힙 자료구조 사용 : 우선순위 큐 ( 가장 우선순위가 높은 데이터 추출)
#===>heapq 사용
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[]for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    #시작노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장 최단거리의 노드 꺼내기
        dist,now=heapq.heappop(q)
        #현재 노드가 이미 처리했다면 무시
        if distance[now]<dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist+i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    #도달할 수 없느 경우
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
