import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 세로, M: 가로
p = []
for i in range(N):
    p.append(list(map(int, input().split())))

from collections import deque

# 바이러스 찾기, O(NM)
def find_v(plain: list):
    q = deque()
    for i in range(len(plain)):
        for j in range(len(plain[i])):
            if plain[i][j] == 2:
                q.append((i, j))
    return q

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스 시뮬레이션
def simulation(plain: list):
    virus = find_v(plain)

    while bool(virus):
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < N and ny >= 0 and ny < M) and plain[nx][ny] == 0:
                plain[nx][ny] = 2
                virus.append((nx, ny))

def getSafeCount(plain: list) -> int:
    count = 0
    for i in range(len(plain)):
        for j in range(len(plain[i])):
            if plain[i][j] == 0:
                count += 1
    return count


print(simulation(p))
print(p)

