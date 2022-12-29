n, m = map(int, input().split())
graph = [ list(map(int, input())) for _ in range(n) ]

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 1 + graph[x][y]
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))