## 미완성 소스코드

def solution(maps):
    n = len(maps)  # x
    m = len(maps[0])  # y

    # (N, M) 으로 접하는 길목이 모두 막혀있는 경우
    if maps[n - 1][m - 2] == 1 and maps[n - 2][m - 1] == 1:
        return -1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y, count):
        if x == n - 1 and y == m - 1:
            return count

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # maps, 0 -> 벽, 1 -> 이동가능
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, count + 1)

    visited = [[False] * m] * n
    print(dfs(x = 0, y = 0, count = 0))

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) # --> 11