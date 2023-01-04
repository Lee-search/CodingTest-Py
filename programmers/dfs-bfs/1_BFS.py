# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque

def solution(numbers, target):
    # numbers = [4, 1, 2, 1]
    # target = 4
    answer = 0  # --> 2

    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])

    while queue:
        total, idx = queue.popleft()
        #print(total, idx)

        if idx < len(numbers) - 1:
            idx += 1
            queue.append([total + numbers[idx], idx])
            queue.append([total - numbers[idx], idx])
        else:
            if total == target:
                answer += 1

    return answer

print(solution([4, 1, 2, 1], 4))