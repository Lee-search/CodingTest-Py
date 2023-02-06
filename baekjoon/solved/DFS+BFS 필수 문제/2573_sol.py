# https://www.acmicpc.net/problem/2573
# 빙산: BFS와 완전탐색 이용
# 문제에 제시된 조건 반드시 확인하기
# ex) 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

import sys
input = sys.stdin.readline
import copy
from collections import deque

n, m = map(int, input().split())
plain = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and plain[nr][nc] >= 1:
                    q.append((nr, nc))
                    visited[nr][nc] = True

# 얼음 부수기 시뮬레이션
def ice_break():
    global plain
    next_plain = copy.deepcopy(plain)

    for i in range(n):
        for j in range(m):
            if plain[i][j] >= 1:
                cnt = 0
                if 0 <= i - 1 < n and plain[i - 1][j] == 0:
                    cnt += 1
                if 0 <= i + 1 < n and plain[i + 1][j] == 0:
                    cnt += 1
                if 0 <= j - 1 < m and plain[i][j - 1] == 0:
                    cnt += 1
                if 0 <= j + 1 < m and plain[i][j + 1] == 0:
                    cnt += 1

                # 남은 빙하보다 0을 접하는 면이 더 많으면 0으로 만들기
                next_plain[i][j] -= cnt if next_plain[i][j] >= cnt else next_plain[i][j]
    plain = next_plain

step = 0
while True:
    block = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 블럭의 개수 세기
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and plain[i][j] >= 1:
                bfs(i, j)
                block += 1
    if block == 0:
        print(0)
        break

    if block >= 2:
        print(step)
        break

    step += 1
    ice_break()