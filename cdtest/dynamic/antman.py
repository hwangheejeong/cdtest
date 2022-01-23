# 개미전사
#연속된 식량창고 약탈 x

import math

n = int(input())
k = list(map(int,input().split()))

mmm = [0]*n

mmm[0] = k[0]
mmm[1] = max(mmm[0],mmm[1])
for i in range(2,n):
    mmm[i]=max(mmm[i-1],mmm[i-2]+k[i])

print(mmm[n-1])


