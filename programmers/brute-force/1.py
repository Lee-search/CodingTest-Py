# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    # 무조건 가로면이 더 길게 만들기
    for i in range(len(sizes)):
        sizes[i] = [max(sizes[i]), min(sizes[i])]

    # 소팅된 명함들 기준 가장 큰 명함 찾기
    max_x, max_y = 0, 0
    for x, y in sizes:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    return max_x * max_y
