N = int(input())
data = list(input().split())

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 초기 위치
x = 1
y = 1

for i in range(len(data)):
    if data[i] == 'R':
        if y < N:
            x += dx[0]
            y += dy[0]
    elif data[i] == 'U':
        if x >1:
            x += dx[1]
            y += dy[1]
    elif data[i] == 'L':
        if y > 1:
            x += dx[2]
            y += dy[2]
    else:
        if x < N:
            x += dx[3]
            y += dy[3]

print(x, y)
