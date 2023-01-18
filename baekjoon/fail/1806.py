# https://www.acmicpc.net/problem/1806
# 부분합: 모든 경우의 수를 다 훑으니 시간초과

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 100001
front, back = 0, 0
total = 0

while True:
    # front - back 사이의 숫자 합이 s보다 크면 리턴
    total += numbers[back]
    #print(front, back, total)

    # 최소 길이 이상으로 연산 X, 시간 단축
    if back - front + 1 >= answer:
        front += 1
        total = 0
        back = front

    if total >= s:
        answer = min(answer, back - front + 1)
        # 길이가 1이면 이보다 더 작아질 수 는 없음
        if front == back:
            break
        front += 1
        total = 0
        back = front

    # 다 더했는데 s 이하인 경우
    elif back >= n:
        break

    else:
        back += 1

print(0 if answer == 100001 else answer)