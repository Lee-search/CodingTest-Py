# https://www.acmicpc.net/problem/16234
# 인구이동: BFS + 구현문제

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x: int, y: int) -> list:
    q = deque()
    q.append((x, y))  # 시작지점 삽입
    
    connected = []    # x, y를 통해 방문하게 되는 국가 리스트
    connected.append((x, y))

    while q:
        r, c = q.popleft()
        #visited[r][c] = True
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 내이면서 다녀가지 않은 곳
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 인구차이가 조건 내인 경우
                if L <= abs(plain[r][c] - plain[nr][nc]) <= R:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    connected.append((nr, nc))  # 연결 정보 추가

    return connected

N, L, R = map(int, input().split())
plain = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0

while True:
    visited = [[False] * N for _ in range(N)]
    changed = False
    for x in range(N):
        for y in range(N):
            # 해당 지점을 과거 루프에서 방문했으면 pass
            if not visited[x][y]:
                visited[x][y] = True
                connected = bfs(x, y)

                # 연결된 다른 나라가 없으면 제외하고 이동
                if len(connected) > 1:
                    changed = True  # 변화 감지
                    avg = sum(list(plain[i][j] for i, j in connected)) // len(connected)

                    for i, j in connected:
                        plain[i][j] = avg

    if changed:
        answer += 1
    # 국경선 닫은 이후에도 변화가 없으면 완료된 것으로 간주, break
    else:
        break

print(answer)