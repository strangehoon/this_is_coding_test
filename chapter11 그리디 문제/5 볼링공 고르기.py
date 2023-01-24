n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

count = 0

# for문을 돌리면서 같은 무게인 경우를 제외하고 count
for i in range(n):
    for j in range(i+1, n):
        if data[i] != data[j]:
            count += 1

print(count)