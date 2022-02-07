#팀 결성
# 0~N번까지의 학생
# 모든 학생이 다른 팀 => 총 N+1개의 팀 존재
# 1) 팀 합치기 : 0 a b
# 2) 같은 팀 연산 확인 : 1 a b
# <같은 팀 여부 확인> 결과 확인
#===> 서로소집합 알고리즘 이용

n,m = map(int,input().split())
graph = []

#각각의 연산 입력
for i in range(m):
    cal, a,b = map(int,input().split())
    graph.append((cal,a,b))

#서로소 알고리즘
#루트 노드 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]


#부모 테이블에서 부모를 자기 자신으로 초기화
parent = [0] *(n+1)
for i in range(1,n+1):
    parent[i] = i

#팀 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#같은 팀 여부 확인
def sameteam(parent,a,b):
    if find_parent(parent,a)==find_parent(parent,b):
        print("YES")
    else:
        print("NO")

for i in graph:
    cal,a,b=i
    #cal=0, 팀합치기
    if cal==0:
        union_parent(parent,a,b)
    #cal=1, 같은팀 여부확인
    else:
        sameteam(parent,a,b)