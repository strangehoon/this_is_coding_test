# 이 문제는 정확성 테스트와 효율성 테스트 전부 통과해야 한다. 아래 코드는 정확성 테스트는 전부 통과 But 효율성 테스트는 전부 실패
# 아래 코드는 O(n)
# 그리디 유형의 문제인데 그리디 개념을 전혀 고려하지 않음

#############################################################################
def solution(food_times, k):
    #  -1을 반환하는 경우
    if sum(food_times) <= k:
        return -1

    # answer : k-1 ~ k 초일때 먹은 음식의 index
    i = 0
    while k != 0:
        if food_times[i % len(food_times)] != 0:
            food_times[i % len(food_times)] -= 1
            k -= 1
            i += 1
        else:
            i += 1
            continue
    answer = i % len(food_times)

    # 네트워크 정상화 후 answer + 1인 음식을 먹어야 하는데 다 먹은 음식은 pass해야한다.
    for j in range(answer, answer + len(food_times)):
        if food_times[j % len(food_times)] == 0:
            continue
        else:
            answer = j % len(food_times)
            break

    # 인덱스(0번부터) -> 몇 번째 음식(1번부터)
    return answer % len(food_times) + 1
