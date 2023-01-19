# https://www.acmicpc.net/problem/1987
# SET 을 이용한 방문탐색에서 시간초과 발생 -> 유사 다익스트라 리스트로 변환 후 해결
import sys, time
input = sys.stdin.readline

t = time.time()

r, c = map(int, input().split())
plain = [list(input()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

idx = set()    # 인덱싱 된 숫자 입력
idx.add(plain[0][0])    # 출발지점 방문처리
answer = 1

def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    # 4 방향 이동 후 이미 idx 된 알파벳 만나면 백트래킹
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < r and 0 <= ny < c:
            if not plain[nx][ny] in idx:
                idx.add(plain[nx][ny])
                dfs(nx, ny, count + 1)
                idx.remove(plain[nx][ny])

dfs(0, 0, answer)
print(answer)
print("time: ", time.time() - t)