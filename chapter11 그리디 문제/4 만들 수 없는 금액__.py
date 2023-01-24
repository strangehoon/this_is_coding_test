import itertools
from itertools import combinations

n = int(input())
coin = list(map(int, input().split()))

# 가능한 모든 코인의 조합
coin_set =  set()

# 가능한 모든 코인의 조합을 coin_set에 저장
for i in range(n):
    ncr = itertools.combinations(coin, i+1)
    for i in ncr:
        coin_set.add(sum(i))

# coin_set에 없는 가장 작은 양의 정수 출력
x = 1
while(True):
    if x not in coin_set:
        print(x)
        break
    else:
        x += 1
