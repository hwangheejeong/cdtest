#부품찾기

n = int(input())

#n개의 정수 입력
arr = list(map(int,input().split()))

#정렬
arr.sort()

m = int(input())
#m개의 정수 입력
x = list(map(int,input().split()))

def binary(arr,target,start,end):
    while start<=end:

        mid = (start+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid+1

    return None

for i in x:
    result = binary(arr,i,0,n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

