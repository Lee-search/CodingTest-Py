# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    # 공간복잡도 고려 X
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    people = [p1, p2, p3]
    match = [0, 0, 0]

    for i, a in enumerate(answers):
        for j in range(3):
            if people[j][i] == a:
                match[j] += 1

    result = []
    for i in range(3):
        if match[i] == max(match):
            result.append(i + 1)
    return result