#1이 될때까지
#1) n-1
#2)n/k
#n이 1이 되는 최소 연산횟수

n,k = map(int,input().split())
count=0

while n>1:
    if n%k==0:
        n=n//k
        count+=1
    else:
        n-=1
        count+=1

print(count)