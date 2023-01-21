n, m = map(int, input().split())
graph = []

# 2차원 리스트의 맵 정보 입력받기
for i in range(n):
    graph.append(list(map(int, input())))

# dfs를 호출하면 해당 노드 주변(상,하,좌,우)의 값들을 모두 1로 바꾼다.
def dfs(i, j):
    graph[i][j] = 1
    if i < n-1 and graph[i+1][j] ==0:
        dfs(i+1, j)
    if i > 0 and graph[i-1][j] ==0:
        dfs(i-1, j)
    if j < m-1 and graph[i][j+1] ==0:
        dfs(i, j+1)
    if j > 0 and graph[i][j-1] ==0:
        dfs(i, j-1)

count = 0

# 모든 노드를 방문, graph의 값이 0일 경우 dfs 호출하고, count 1증가
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)