# 내가 푼 방식은 시간 복잡도가 O(n^2)으로 좋지 않은 알고리즘이다. 하지만 문제에서 n이 최대 1000까지 가능하고 시간 제한이 1초이므로 O(n^2)이여도 문제 없다.
# 아래 풀이는 시간 복잡도가 O(n)인 풀이다.

#############################################################################

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 1인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)