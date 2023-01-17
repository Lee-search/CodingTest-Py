n, m = map(int, input().split())
plain = []
for _ in range(n):
    line = input()
    plain.append([int(line[i]) for i in range(m)])

visited = [[False] * m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 9999
def dfs(r, c):
    if r == n - 1 and c == m - 1:
        global answer
        answer = min(answer, plain[r][c])

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                plain[nr][nc] = plain[r][c] + 1
                dfs(nr, nc)
                visited[nr][nc] = False

dfs(0, 0)
print(answer)