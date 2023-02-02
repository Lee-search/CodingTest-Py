# https://softeer.ai/practice/info.do?idx=1&eid=409
# 장애물 인식 프로그램: DFS
import sys
input = sys.stdin.readline

n = int(input())
plain = []
for _ in range(n):
    plain.append(list(map(int, list(input().replace('\n', '')))))

visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위 바깥 예외처리
        if 0 <= nx < n and 0 <= ny < n:
            # 방문하지 않은 노드에 대해
            if not visited[nx][ny]:
                # 1인지 0인지 확인
                if plain[nx][ny] == 1:
                    dfs(nx, ny)

# MAIN
cnt_arr = []
for i in range(n):
    for j in range(n):
        # 과거에 방문하였거나 장애물이 없으면 넘어감
        if visited[i][j] or plain[i][j] == 0:
            continue

        count = 0
        dfs(i, j)
        cnt_arr.append(count)

print(len(cnt_arr))
for k in sorted(cnt_arr):
    print(k)
