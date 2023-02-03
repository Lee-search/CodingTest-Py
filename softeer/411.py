import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())    # n: 세로, m: 가로
plain = []
ice_count = 0
for _ in range(n):
    line = list(map(int, input().split()))
    ice_count += line.count(1)
    plain.append(line)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and plain[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))

visited = [[False for _ in range(m)] for _ in range(n)]
step = 0
while ice_count > 0:

    for i in range(n):
        for j in range(m):
            # 얼음 칸이거나
            if plain[i][j] == 1:
                continue
            # 이미 지나간 경로이면 넘어감
            if visited[i][j]:
                continue

            # i, j 칸에 대해
            # 한 칸이라도 외부와 접하는 면이 있으면 BFS 실행
            for d in range(4):
                ni = i + dr[d]
                nj = j + dc[d]
                if ni < 0 or ni > n or nj < 0 or nj > m:
                    bfs(i, j)
                    break

    for i in range(n):
        for j in range(m):
            if visited[i][j]:


    step += 1
    print(plain)
    print(visited)
print(step)