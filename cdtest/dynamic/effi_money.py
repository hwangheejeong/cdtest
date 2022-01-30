# 효율적인 화폐구성
# 최소한의 화폐개수

# 화폐개수 n개, 각 화폐의 단위 입력
n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in money:
   if i <=m:
       d[i]=1

for i in money:
    for j in range(i+1,m+1):
        d[j]=min(d[j],d[j-i]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
