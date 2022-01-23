#두 배열이 원소교체

n,k = map(int,input().split())
a = map(int,input().split())
b = map(int,input().split())

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break;

print(sum(a))

