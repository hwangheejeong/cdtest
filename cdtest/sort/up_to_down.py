#내림차림 정렬
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

#오름차림 => sorted(arr)
#내림차림 => reverse=True
result = sorted(arr, reverse=True)

print(result)