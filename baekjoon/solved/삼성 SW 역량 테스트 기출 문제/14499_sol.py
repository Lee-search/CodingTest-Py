# https://www.acmicpc.net/problem/14499
# 주사위굴리기: 구현, 시뮬레이션

N, M, x, y, K = list(map(int, input().split()))
plain = [] # 지도
command = [] # 명령
for _ in range(N):
    plain.append(list(map(int, input().split())))
command = list(map(int, input().split()))

def getPoint(x: int, y: int, direct: int):
    if direct == 1: # East
        x, y = x, y + 1
    elif direct == 2: # West
        x, y = x, y - 1
    elif direct == 3: # North
        x, y = x - 1, y
    else: # South
        x, y = x + 1, y

    return x, y

def getDice(direct: int, dice: list):
    if direct == 1: # East
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif direct == 2: # West
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif direct == 3: # North
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    else:   # South
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    return dice

dice = [0, 0, 0, 0, 0, 0, 0]
for i in range(K):
    d = command[i]
    t_x, t_y = x, y
    x, y = getPoint(x, y, d)
    if x < 0 or x > N - 1 or y < 0 or y > M - 1: # OOR
        x, y = t_x, t_y
        continue

    dice = getDice(d, dice)
    if plain[x][y] == 0:
         plain[x][y] = dice[6]
    else:
        dice[6] = plain[x][y]
        plain[x][y] = 0

    print(dice[1]) # 주사위 윗부분 출력
