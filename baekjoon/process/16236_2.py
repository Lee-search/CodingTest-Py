from collections import deque

N = int(input())
graph = []
visited = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
    visited.append([False] * N)

# 상어 객체 정의
class Shark:
    row, col = -1, -1   # 좌표
    size = 2    # 크기
    c_move = 0  # 이동횟수
    c_eat = 0   # 먹은생선수

    def __init__(self):
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 9:
                    self.row, self.col = i, j
                    break

    def update(self):
        if self.c_eat == self.size:
            self.size += 1
            self.c_eat = 0

# BFS, 이동가능한 모든 위치 탐색
def move(r: int, c: int, d: int) -> (int, int):
    # N, E, S, W
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    return r + dr[d], c + dc[d]

def BFS(S: Shark):
    moved = 0
    q = deque()
    q.append((S.row, S.col))

    while q != deque():
        r, c = q.popleft()
        if 0 < graph[r][c] < S.size:
            print('r, c :', (r, c))
            print(q)

            graph[r][c] = 9
            graph[S.row][S.col] = 0

            S.row, S.col = r, c
            S.c_move += moved
            S.c_eat += 1
            S.update()

            moved = 0

            q.clear()
            q.append((S.row, S.col))
            for _ in range(N):
                visited.append([False] * N)
            continue

        for i in range(4):
            nr, nc = move(r, c, i)
            if (0 <= nr < N and 0<= nc < N) and graph[nr][nc] <= S.size and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
        moved += 1

S = Shark()
BFS(S)
print(S.c_move)