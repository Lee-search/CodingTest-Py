N, M = list(map(int, input().split()))  # 세로, 가로
x, y, d = list(map(int, input().split()))   # 위치, 방향

plain = []
for _ in range(N):
    plain.append(list(map(int, input().split())))

cleand= 0   # 청소횟수
searched = 0

while True:
    print((x, y, d), 's_count= ', searched)

    if searched == 4:
        if d == 0 and plain[x+1][y] != 1:
            x = x + 1
            searched = 0
        elif d == 1 and plain[x][y-1] != 1:
            y = y - 1
            searched = 0
        elif d == 2 and plain[x-1][y] != 1:
            x = x - 1
            searched = 0
        elif d == 3 and plain[x][y+1] != 1:
            y = y + 1
            searched = 0
        else:
            print(cleand)
            break

    if d == 0 and (y - 1) > 0:  # North
        d = 3  # 왼쪽으로 회전
        searched += 1

        if plain[x][y-1] == 0:  # 청소 안되어있으면 이동 후 청소
            y = y - 1
            plain[x][y] = 1
            cleand += 1

    elif d == 1 and (x - 1) > 0:    # East
        d = 0
        searched += 1

        if plain[x-1][y] == 0:
            x = x - 1
            plain[x][y] = 1
            cleand += 1

    elif d == 2 and (y + 1) < M:    # South
        d = 1
        searched += 1

        if plain[x][y+1] == 0:
            y = y + 1
            plain[x][y] = 1
            cleand += 1

    elif d == 3 and (x + 1) < N:    # West
        d = 2
        searched += 1

        if plain[x+1][y] == 0:
            x = x + 1
            plain[x][y] = 1
            cleand += 1
