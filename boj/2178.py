from collections import deque

# 행, 열
n, m = map(int, input().split())
plain = []
for _ in range(n):
    plain.append(list(map(int, list(input()))))

visited = [[False] * m] * n

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr: int, sc: int):
    queue = deque([(sr, sc, 1)])
    visited[sr][sc] = True

    while queue:

        print(queue)
        r, c, moved = queue.popleft()

        if r == n - 1 and c == m - 1:
            print(moved)
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and plain[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc, moved + 1))
                visited[nr][nc] = True


bfs(0,0)

print(plain)