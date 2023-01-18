# https://www.acmicpc.net/problem/1806
# 부분합: 이중 포인터 사용

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 100001
left, right = 0, 0
total = 0

while True:
    # right 포인터가 끝까지 이동 -> 더이상 s 이상일 수 없음
    # total < s 조건 없으면 반례 1 1 1 1 1 1 1 1 1 10 -> 0
    if right == n and total < s:
        break

    # s보다 큰 경우의 최소 길이 구함
    if total >= s:
        answer = min(answer, right - left)
        total -= numbers[left]
        left += 1
    # s보다 커질 때 까지 포인터 이동
    else:
        total += numbers[right]
        right += 1
    #print(left, right, total)


print(0 if answer == 100001 else answer)