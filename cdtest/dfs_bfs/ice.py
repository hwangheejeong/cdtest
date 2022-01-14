#dfs
#음료수 얼려먹기

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    #범위 -1<x<n , -1<y<m
    if x<=-1 or x>=n or y>=m or y<=-1:
        return False
    #방문하지 않은 노드
    if graph[x][y]==0:
        #방문 처리
        graph[x][y]=1
        #상하좌우 재귀
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)