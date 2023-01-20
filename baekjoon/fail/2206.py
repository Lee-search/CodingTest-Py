# 벽을 부수고 방문 하는 경우 visited 에 표기하면
# 벽을 부수지 않고 이동하는 경우에 해당 블럭에 도달할 수 없음
# idea: https://www.acmicpc.net/board/view/106323

from collections import deque

n, m = map(int, input().split())
plain = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = int(1e9)

def bfs(x, y):
    global answer
    queue = deque()
    # 처음 방문한 지점은 항상 0 이라고 가정
    # 초기좌표 x, y, 이동 횟수, 벽 부수기 여부
    queue.append((x, y, 1, False))
    visited[x][y] = True

    while queue:
        x, y, count, flag = queue.popleft()
        if x == n - 1 and y == m - 1:
            answer = min(answer, count)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if plain[nx][ny] == 0:
                    #print(nx, ny)
                    queue.append((nx, ny, count + 1, flag))
                    visited[nx][ny] = True
                # 벽 부수기 안썼으면 -> 쓰고 큐에 삽입
                elif not flag:
                    #print(nx, ny)
                    queue.append((nx, ny, count + 1, not flag))
                    visited[nx][ny] = True

    print(answer if answer != int(1e9) else -1)

bfs(0, 0)