#바닥 공사

n = int(input())

#다이나믹
d =[0]*1001

d[1]=1
#2x2 => 3가지 경우의 수 (1x2=>2개, 2x1=>2개, 2x2=>1개)
d[2]=3

for i in range(3,n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[n])
