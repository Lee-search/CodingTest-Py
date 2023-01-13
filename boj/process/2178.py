from collections import deque

n, m = map(int, input().split())
plain = []
for _ in range(n):
    line = input()
    plain.append([int(line[i]) for i in range(m)])

visited = [[False] * m for _ in range(n)]

def bfs(sx, sy):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = deque()
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if plain[nx][ny] == 0:
                continue

            if plain[nx][ny] == 1:
                plain[nx][ny] = 1 + plain[x][y]
                queue.append((nx, ny))

    return plain[n - 1][m - 1]

print(bfs(0, 0))