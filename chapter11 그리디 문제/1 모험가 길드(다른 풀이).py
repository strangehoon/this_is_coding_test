n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in range(len(data)):
    count += 1
    if count == data[i]:
        count = 0
        result += 1
print(result)