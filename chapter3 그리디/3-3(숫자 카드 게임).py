n, m = map(int, input().split())

min_list = []

# 각 행에서 가장 작은 값을 min_list에 추가
for i in range(n):
    min_list.append(min(list(map(int, input().split()))))

# min_list 값들 중 가장 큰 값 출력
print(max(min_list))