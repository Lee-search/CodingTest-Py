# https://www.acmicpc.net/problem/2667
# 번호붙히기: DFS
import sys
input = sys.stdin.readline

n = int(input())
plain = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global total
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if plain[nx][ny] != 1:
            continue
        if visited[nx][ny]:
            continue

        total += 1
        visited[nx][ny] = True
        dfs(nx, ny)

blocks = []
for i in range(n):
    for j in range(n):
        if plain[i][j] == 1:
            if not visited[i][j]:
                total = 1
                visited[i][j] = True
                dfs(i, j)
                blocks.append(total)

blocks.sort()
print(len(blocks))
for i in range(len(blocks)):
    print(blocks[i])