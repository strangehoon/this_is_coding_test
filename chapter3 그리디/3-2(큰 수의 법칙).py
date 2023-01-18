n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 내림차순 정렬
data.sort(reverse=True)

# 가장 큰 수 k개와 두번째로 큰 수 1개가 반복되는 수열을 이룸
quotient = m // (k+1)
remainder = m % (k+1)

result = (data[0]*k + data[1])*quotient + remainder*data[0]

print(result)


