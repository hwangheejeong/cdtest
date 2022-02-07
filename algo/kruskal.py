# 크루스칼 알고리즘 (시간복잡도 : O(ElogE)
# => 가장 거리가 짧은 간선부터 집합에 포함
#    사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함x
# 1) 간선 오름차순
# 2) 사이클 확인
#    사이클 발생 x => 최소신장트리에 포함
#    사이클 발생 o => 포함x
# 3) 모든 간선에 대해 2번 반복


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


#노드의 개수와 간선의 개수 입력받기
v,e = map(int,input().split())
parent = [0] *(v+1)

#모든 간선을 담을 리스트와 최종비용을 담을 변수
edges = []
result = 0

#부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인
for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않을 경우, 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)