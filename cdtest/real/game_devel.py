#게임개발
#바다 : 1 육지 :0
#현재 방향을 기준으로 왼쪽으로(반시계방향)
#현재 위치 (A,B)
#바라보는 방향(d) ==> 북:0  동:1  남:2  서:3
#맵위 외곽은 항상 바다 ==> 테두리는 1


#NxM 설정
n,m = map(int,input().split())

#현재위치 , 바라보고 있는 방향
a,b,d = map(int,input().split())
loc = (a,b)

#map 만들기(바다/육지)
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))

#방문여부 리스트 만들기
visited =[[False]*m]*n

#이동칸 : 북 (a-1,b) 동 (a,b+1) 남 (a+1,b) 서 (a,b-1)
move = [(-1,0),(0,1),(1,0),(0,-1)]

#dd = [0,3,2,1]
#반시계방향 d의 순서 (0-3-2-1)
def turn(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    elif d==3:
        return 2

#나의 위치
def my(d,loc):
    if d==0:
        loc = [x + y for x, y in zip(loc, move[0])]
    elif d==1:
        loc = [x + y for x, y in zip(loc, move[1])]
    elif d==2:
        loc = [x + y for x, y in zip(loc, move[2])]
    elif d==3:
        loc = [x + y for x, y in zip(loc, move[3])]

#이동한 뒤의 위치
a=loc[0]
b=loc[1]

#바다:1이면 이동 불가
#방문한곳 이동 불가
#상하좌우 이동가능 확인
def go(d):
    for _ in range(4):
        if list[a][b] == 1:
            d = turn(d)
        else:
            if visited[a][b]==True:
                d = turn(d)
            else:
                visited[a][b]=1
                return my(d,loc)
    return d

#후진
def rev(d,loc):
    if d == 0:
        loc = [x + y for x, y in zip(loc, move[2])]
    elif d == 1:
        loc = [x + y for x, y in zip(loc, move[3])]
    elif d == 2:
        loc = [x + y for x, y in zip(loc, move[0])]
    elif d == 3:
        loc = [x + y for x, y in zip(loc, move[1])]

#위치가 안변하면 뒤로
if loc==go(d) and loc[a][b]==0:
    rev(d,loc)

go(d)

