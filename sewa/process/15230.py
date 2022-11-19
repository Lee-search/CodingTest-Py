N = int(input())

origin = 'abcdefghijklmnopqrstuvwxyz'
for test in range(1, N + 1):
    mine = input()
    best, cnt = 0, 0

    i = 0
    for n in range(len(mine)):
        if mine[n] != origin[i]:
            best = max(best, cnt)
            cnt = 0
            i = 0
        if mine[n] == origin[i]:
            i += 1
            cnt += 1
    best = max(best, cnt)

    print(f'#{test} {best}')