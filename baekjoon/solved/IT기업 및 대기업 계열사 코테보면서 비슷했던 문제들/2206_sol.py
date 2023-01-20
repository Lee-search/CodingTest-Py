# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기 : BFS 인데 visited 리스트를 3중 배열로 사용하여야함

from collections import deque

n, m = map(int, input().split())
plain = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = int(1e9)

def bfs(x, y):
    global answer
    queue = deque()
    # 처음 방문한 지점은 항상 0 이라고 가정
    # 초기좌표 x, y, move_count, 남은 벽 부수기 횟수
    queue.append((x, y, 1, 1))
    visited[x][y][1] = True

    while queue:
        x, y, move_count, wall_left = queue.popleft()
        if x == n - 1 and y == m - 1:
            answer = min(answer, move_count)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if plain[nx][ny] == 0 and not visited[nx][ny][wall_left]:
                    #print(nx, ny)
                    queue.append((nx, ny, move_count + 1, wall_left))
                    visited[nx][ny][wall_left] = True
                # 벽 부수기 안썼으면 -> 쓰고 큐에 삽입
                if plain[nx][ny] == 1 and wall_left == 1:
                    #print(nx, ny)
                    queue.append((nx, ny, move_count + 1, wall_left - 1))
                    visited[nx][ny][wall_left - 1] = True

    print(answer if answer != int(1e9) else -1)

bfs(0, 0)