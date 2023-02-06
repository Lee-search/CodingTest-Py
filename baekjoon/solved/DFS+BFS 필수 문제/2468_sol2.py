# https://www.acmicpc.net/problem/2468
# 안전 영역: DFS
# setrecursionlimit 함수를 통해 재귀문의 반복 깊이를 확장하였음
# pypy로 풀면 메모리 초과, python3 로 클리어

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# 재귀 반복 깊이 최대값 :
# n * n * depth = 100 * 100 * 100 = 1000000

n = int(input())
plain = []

for i in range(n):
    plain.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    visited[r][c] = True

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 범위 바깥부분 예외처리
        if 0 <= nr < n and 0 <= nc < n:
            # 이미 방문한 곳 & 물에 잠기는 곳 제외
            if not visited[nr][nc] and plain[nr][nc] > depth:
                dfs(nr, nc)

answer = 1  # 블럭의 수
depth = 0   # 잠긴 물의 높이

while depth <= 100:
    block = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and plain[i][j] > depth:
                dfs(i, j)
                block += 1

    answer = max(answer, block)
    depth += 1
print(answer)