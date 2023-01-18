data = input()
x = data[0]
y = int(data[1])
x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 알파벳을 정수로 변환,  --> ord()를 사용하면 아스키코드값을 뽑을 수 있음.
x = x_list.index(x) + 1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0

# 이동한 나이트가 체스판 안에 존재하면 count 1 증가
for i in range(len(dx)):
    if (1<= x + dx[i] <= 8) and (1 <= y + dy[i] <= 8):
        count += 1
print(count)
