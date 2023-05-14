# https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    for y in range(yellow, 0, -1):
        if yellow % y == 0:
            # 가능한 가로, 세로 길이 구하기
            row, col = y, yellow // y

            # 조건에 맞는지 확인
            if (row + 2) * 2 + col * 2 == brown:
                return [row + 2, col + 2]