# https://www.acmicpc.net/problem/2468
# 안전영역: BFS 로 풀었으나 DFS도 가능할 것 같음

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
plain = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc, depth):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and plain[nr][nc] > depth:
                    q.append((nr, nc))
                    visited[nr][nc] = True

answer = 0  # 가능한 많은 블럭 수
depth = 0   # 물의 높이

while depth <= 100:
    block = 0   # 반복문 시작 시 visited 초기화 필요
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and plain[i][j] > depth:
                bfs(i, j, depth)
                block += 1

    answer = max(answer, block)
    depth += 1
print(answer)