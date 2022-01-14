# 떡복이 만들기

#떡개수 , 원하는 길이
n,m = map(int,input().split())

#각 떡의 길이
len=list(map(int,input().split()))

s,e=0,max(len)
result=0
#mid는 절단기 높이
while (s<=e):
    mid = (s+e)//2
    #총 잘린 길이
    total =0
    for i in len:
        #떡의 길이가 절단기보다 길면 잘린 값 더하기
        if i-mid>0:
            total+=i-mid
    #m이 total보다 크거나 같으면 일단 result값 저장
    if total<m:
        e=mid-1
    else:
        result = mid
        s=mid+1

print(result)

