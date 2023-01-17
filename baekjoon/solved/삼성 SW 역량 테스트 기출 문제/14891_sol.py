# https://www.acmicpc.net/problem/14891
# 톱니바퀴: 구현, 시뮬레이션

import sys
input = sys.stdin.readline

from collections import deque
gears = [{}]  # 톱니 4개, 0번은 사용 X

for _ in range(4):
    gears.append(deque(map(int, input().replace('\n', ''))))

k = int(input())  # 회전 횟수
orders = []  # 회전 명령 (번호, 방향)
for _ in range(k):
    orders.append(list(map(int, input().split())))

def check_left(l: int, d: int):
    # 왼쪽에 더이상 기어가 없음 or 왼쪽과 가운데가 같은 극
    if l < 1 or gears[l][2] == gears[l + 1][6]:
        return

    # 다른 극 끼리 만났으면 왼쪽 확인 하고 회전
    if gears[l][2] != gears[l + 1][6]:
        check_left(l-1, -d)
        gears[l].rotate(d)

def check_right(r: int, d: int):
    if r > 4 or gears[r-1][2] == gears[r][6]:
        return

    if gears[r - 1][2] != gears[r][6]:
        check_right(r+1, -d)
        gears[r].rotate(d)

for o in orders:
    g = o[0]    # 기어번호
    d = o[1]    # 회전방향

    check_left(g - 1, -d)
    check_right(g + 1, -d)
    gears[g].rotate(d)

print(sum(2 ** (i - 1) for i in range(1, 5) if gears[i][0] == 1))
