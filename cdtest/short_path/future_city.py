#플로이드 워셜 알고리즘
INF = int(1e9)
n,m = map(int, input().split())

#무한으로 초기화
# n+1 => 인덱스값 = 회사번호
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신으로 가는 비용 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k]+graph[k][x]

if distance>=INF:
    print("-1")
else:
    print(distance)