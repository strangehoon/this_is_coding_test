N, K = map(int, input().split())

count = 0
while(N >= K):
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    count += N - (N//K)*K

    N = (N//K)*K

    # K로 나누기
    N //= K
    count +=1

# 마지막으로 남은 수에 대하여 1씩 빼기
count += N-1
print(count)

