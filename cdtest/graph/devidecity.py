#도시분할계획 => 최소신장트리(크루스칼)
# 두개의 분리된 마을 => 각 마을은 단절
#크루스칼 알고리즘을 이용해 최소신장트리를 구하고,
# 그 중 비용이 가장 큰 간선 빼주기 (2개의 도시)


n,m = map(int,input().split())
graph = []
for i in range(m):
    a,b,c = map(int,input().split()) #a집과 b집을 지나가는데 드는 비용 c
    graph.append((c,a,b)) #비용순으로 정렬해야하므로 리스트 맨 앞에 비용

#비용순으로 정렬
graph.sort()


#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent = [0] *(n+1)

result = 0

#부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i


#간선을 하나씩 확인
for edge in graph:
    c,a,b = edge
    #사이클이 발생하지 않을 경우, 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        cost=c
        result+=c

print(result-cost)