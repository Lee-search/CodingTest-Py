# https://www.acmicpc.net/problem/20055
# 컨베이어벨트: 구현, 시뮬레이션, Deque 내부 rotate 함수 이용
from collections import deque

n, k = map(int, input().split())
# 벨트 내구도
belt_arr = deque(list(map(int, input().split())))
# 로봇 위치
robots = deque([0] * n)

step = 0
while True:
    step += 1

    # 1. 벨트 & 로봇 회전
    belt_arr.rotate(1)
    robots[-1] = 0
    robots.rotate(1)
    robots[-1] = 0

    # 2. 로봇 이동, n = 3, 1 -> 0 확인
    for i in range(n - 2, -1, -1):
        if belt_arr[i + 1] >= 1 and robots[i + 1] == 0 and robots[i] == 1:
            robots[i + 1] = 1
            robots[i] = 0
            belt_arr[i + 1] -= 1
    
    # 3. 로봇 올리기
    if robots[0] == 0 and belt_arr[0] >= 1:
        robots[0] = 1
        belt_arr[0] -= 1

    # 4. 내구도 검증
    if belt_arr.count(0) >= k:
        break

print(step)