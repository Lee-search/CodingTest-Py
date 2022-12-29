n, m = map(int, input().split())
# 지도 생성, N x M
visit = [[0] * m] * n

# 시작 지점 입력
x, y, direct = map(int, input().split())
visit[x][y] = 1 # 시작 지점 방문

plain = [ list(map(int, input().split())) for _ in range(n) ]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d: int):
    d -= 1
    if d == -1: d = 3

    return d

count = 1
turned = 0
while True:
    direct = turn_left(direct)
    turned += 1
    nx, ny = x + dx[direct], y + dy[direct]

    if visit[nx][ny] == 0 and plain[nx][ny] == 0:
        x, y = nx, ny   # move
        visit[nx][ny] = 1
        turned = 0
        count += 1
        continue

    else:
        turned += 1

    if turned == 4:
        nx, ny = x - dx[direct], y - dy[direct]
        if plain[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turned = 0

print(count)
