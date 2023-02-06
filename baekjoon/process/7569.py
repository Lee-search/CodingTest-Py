from collections import deque
import sys
input = sys.stdin.readline

# 가로, 세로, 높이
M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
# 위, 아래, 북, 동, 남, 서
moves = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)]

last_day = 0

# 시작지점의 높이, 세로, 가로
def bfs(sh, sr, sc):
    q = deque()
    q.append((sh, sr, sc, 0))
    visited[sh][sr][sc] = True

    day = 0
    while q:
        h, r, c, day = q.popleft()

        for i, j, k in moves:
            nh, nr, nc = h + i, r + j, c + k
            # 범위 바깥인 경우
            if nh < 0 or nh > H or nr < 0 or nr > N or nc < 0 or nc > M:
                continue
                
            # 토마토가 없는 칸인 경우
            if boxes[nh][nr][nc] == -1:
                continue
            
            # 이미 방문한 경우
            if visited[nh][nr][nc]:
                continue

            visited[nh][nr][nc] = True
            q.append((nh, nr, nc, day + 1))



for i in range(h):

print()