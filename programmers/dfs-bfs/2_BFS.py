from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque()
    queue.append([0, 0])  # x, y, count

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        c_x, c_y = queue.popleft()
        # (x, y)가 끝에 도달 한 경우
        if c_x == n - 1 and c_y == m - 1:
            return maps[c_x][c_y]

        for d in range(4):
            n_x = c_x + dx[d]
            n_y = c_y + dy[d]
            if 0 <= n_x < n and 0 <= n_y < m:
                if maps[n_x][n_y] == 1:
                    maps[n_x][n_y] = maps[c_x][c_y] + 1
                    queue.append([n_x, n_y])
    
    # 끝에 도달하지 않았는데 queue가 비어있음 -> 끝에 도달하지 못함
    if maps[n - 1][m - 1] == 1:
        return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))