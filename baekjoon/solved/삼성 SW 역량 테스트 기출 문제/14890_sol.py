# https://www.acmicpc.net/problem/14890
# 경사로: 구현

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
roads = []

for _ in range(N):  # Get N
    roads.append(list(map(int, input().split())))

for i in range(N):  # Get 2N
    temp = []
    for j in range(N):
        temp.append(roads[j][i])
    roads.append(temp)

def check_back(l: list, L: int, pos: int) -> bool:
    if pos - (L - 1) < 0:
        return False
    for i in range(pos - (L - 1), pos + 1):
        if not l[i]:
            return False
    return True

def set_back(l: list, L: int, pos: int):
    for i in range(pos - (L - 1), pos + 1):
        l[i] = False

def check_front(l: list, L: int, pos: int) -> bool:
    if pos + L > N - 1:
        return False
    for i in range(pos + 1, pos + L + 1):
        if not l[i]:
            return False
    return True

def set_front(l: list, L: int, pos: int):
    for i in range(pos + 1, pos + L + 1):
        l[i] = False

##### MAIN #####
count = 0
for k in range(2 * N):
    # 모든 길에 대해서 검증 시작
    r = roads[k]
    l = [True] * N

    for pos in range(len(r)):
        if pos == len(r) - 1:  # 마지막 칸이면 -> 종료
            count += 1
            #print(r)
            #print(l)
            break

        # 다음 칸이 경사가 같으면,
        if r[pos] == r[pos + 1]:
            continue

        # 1. 올라가야 하는 경우,
        if r[pos] + 1 == r[pos + 1]:
            if check_back(l, L, pos):
                set_back(l, L, pos)
                continue
            break

        # 2. 내려가야 하는 경우,
        elif r[pos] - 1 == r[pos + 1]:
            if check_front(l, L, pos):
                set_front(l, L, pos)
                continue
            break

        else:
            break  # 이동가능한 모든 케이스 조회

print(count)

