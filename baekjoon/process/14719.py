h, w = map(int, input().split())
heights = list(map(int, input().split()))
blocks = [[1] * w for _ in range(h)]

# blocks: 블록 있으면 0 없으면 1
for c in range(w):
    for r in range(h - 1, h - 1 - heights[c], -1):
        blocks[r][c] -= 1
print(blocks)
from collections import deque

def bfs(r: int, sc: int) -> bool:
    visited = [False] * w
    q = deque()
    q.append(sc)
    visited[sc] = True

    while q:
        c = q.popleft()
        # 좌우 이동
        for nc in [c - 1, c + 1]:
            print(r, nc)
            if nc < 0 or nc >= w:
                return False
            # 방문한 곳, 블럭 있는 곳 제외
            if visited[nc] or blocks[r][nc] == 0:
                continue

            q.append(nc)
            visited[nc] = True
    return True

# 물이 있는 칸에 대해 좌우로 물이 넘치는지 검증
for r in range(h):
    for c in range(w):
        if blocks[r][c] == 1:
            if not bfs(r, c):
                blocks[r][c] -= 1

print(blocks)
print(sum(list(sum(blocks[i]) for i in range(h))))