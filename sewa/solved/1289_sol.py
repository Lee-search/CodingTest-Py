N = int(input())
for test in range(1, N + 1):
    origin = list(map(int, list(input())))
    mine = [0] * len(origin)

    cnt = 0
    for i in range(len(origin)):
        if origin[i] != mine[i]:
            mine = mine[:i] + [origin[i]]  * (len(origin) - i)
            cnt += 1

    print(f'#{test} {cnt}')