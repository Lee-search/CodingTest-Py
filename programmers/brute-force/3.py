# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations

def solution(numbers):
    answer = 0

    numbers = list(numbers)
    new_nums = []

    for i in range(1, len(numbers) + 1):
        # 가능한 모든 수 생성
        p_nums = list(permutations(numbers, i))
        p_nums = list(map(list, p_nums))
        p_nums = ["".join(each) for each in p_nums]
        p_nums = list(map(int, p_nums))

        new_nums.extend(p_nums)

    # 검증을 위해 중복 제거 후 정렬
    new_nums = list(set(new_nums))

    for each in new_nums:
        if each == 0 or each == 1:
            continue
        elif each == 2 or each == 3:
            answer += 1
            continue

        # 4인 경우, [2, 3] 검증
        flag = False
        for i in range(2, each):
            # 중간에 나누어지는 수가 있으면 소수 아님
            if each % i == 0:
                flag = not flag
                break

        if not flag:
            answer += 1

    return answer

