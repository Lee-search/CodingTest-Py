# dijkstra 문제를 dfs 로 구현하였으나 타임에러

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, total):
    if r == n - 1 and c == n - 1:
        global answer
        # print(total)
        answer = min(answer, total)
        return
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    dfs(nr, nc, total + plain[nr][nc])
                    visited[nr][nc] = False

import time

idx = 1
while True:
    n = int(input())
    if n == 0:
        break

    t = time.time()

    plain = []
    for _ in range(n):
        plain.append(list(map(int, input().split())))

    visited =[[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    answer = 9999

    dfs(0, 0, plain[0][0])
    print(f'Problem {idx}: {answer}')
    idx += 1
    print(time.time() - t)
print("exit..")