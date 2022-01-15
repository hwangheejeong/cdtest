#다익스트라
#시간복잡도 => O(V^2) , V는 노드의 개수

import sys

input = sys.stdin.readline   #input()보다 빠른 readline
INF = int(1e9)               #초기값 무한

#노드의 개수 간선의 개수
n,m = map(int,input().split())
#시작노드 번호
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트
visited = [False]*(n+1)
#최단거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

#모든 간선의 정보
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))         #a에서 b노드로 가는 비용이 c

#다음 방문할 노드 반환
#---> 방문하지 않은 노드 중,가장 최단거리가 더 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0   #가장 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i

    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True      #방문처리
    for j in graph[start]:
        distance[j[0]]=j[1]    #start와 연결된 노드들의 첫 값
    #시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단거리가 가장 짧은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now]=True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now]+j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    #도달할 수 없느 경우
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])