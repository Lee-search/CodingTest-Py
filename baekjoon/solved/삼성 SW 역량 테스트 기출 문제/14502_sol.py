# https://www.acmicpc.net/problem/14502
# 연구소: 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 세로, M: 가로
plain = []
for i in range(N):
    plain.append(list(map(int, input().split())))

from collections import deque

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스 시뮬레이션
def simulation(p: list) -> int:
    # 바이러스 찾기
    virus = deque((i, j) for i in range(len(p)) for j in range(len(p[i])) if p[i][j] == 2)

    while virus:    # BFS
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < N and ny >= 0 and ny < M) and p[nx][ny] == 0:
                p[nx][ny] = 2
                virus.append((nx, ny))

    # 0 갯수 찾기
    s = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == 0:
                s += 1
    return s

# 시작 단계에서 안전구역 탐색
safes = deque((i, j) for i in range(len(plain)) for j in range(len(plain[i])) if plain[i][j] == 0)

# Maximum Safe Area
max_safe = 0

# idea from https://cotak.tistory.com/14
for i in range(len(safes)):
    for j in range(i + 1, len(safes)):
        for k in range(j + 1, len(safes)):
            w_1 = safes[i]
            w_2 = safes[j]
            w_3 = safes[k]

            p = copy.deepcopy(plain)
            p[w_1[0]][w_1[1]] = 1
            p[w_2[0]][w_2[1]] = 1
            p[w_3[0]][w_3[1]] = 1
            max_safe = max(max_safe, simulation(p))

print(max_safe)