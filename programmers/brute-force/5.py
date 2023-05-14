# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3

from itertools import permutations

def solution(k, dungeons):
    brute_force = list(permutations(range(len(dungeons))))
    answer = 0

    for i in range(len(brute_force)):
        result = 0
        now_k = k
        for mv in brute_force[i]:
            # dungeons -> 최소피로도, 소모피로도
            if dungeons[mv][0] > now_k:
                break
            else:
                result += 1
                now_k -= dungeons[mv][1]

        answer = max(result, answer)
    return answer
