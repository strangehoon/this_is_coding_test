# 나는 파이썬 그리디 방식으로 풀지 않고 파이썬 itertools의 combinations를 사용해서 풀었다. 하지만 아래와 같이 그리디 방식으로도 풀 수 있다.
# 아래 방식이 더 직관적이며 성능이 더 좋다.

#############################################################################

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < i:
        break
    target += i

# 만들 수 없는 금액 출력
print(target)