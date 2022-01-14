# 숫자카드게임
# 가장 높은 숫자카드 뽑기
##Hint
# 1) 각 행의 최솟값 구하기
# 2) 최솟값 중 최대값 구하기

# NxM
N, M = map(int, input().split())
result =0

# data = []
# for i in range(N):
#     data.append(list(map(int, input().split())))
#
# # 각 행의 최솟값 구하기
# d_min = []
# for i in range(N):
#     d_min.append(min(data[i]))
#
# # 최솟값 중 최대값이 존재하는 행의 인덱스값 구하기
# result = max(d_min)


### 각 행의 최솟값 구하고 최대값인지 확인
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
