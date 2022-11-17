# https://velog.io/@mein-figur/SWEAPython1220.-Magnetic

for test in range(1, 11):
    N = int(input())
    plain = []

    for _ in range(N):
        plain.append(list(map(int, input().split())))

    cnt = 0
    for c in range(N):
        flag = False
        for r in range(N):
            target = plain[r][c]
            if target == 1:
                flag = True
            elif target == 2:
                if flag:
                    cnt += 1
                    flag = False

    print(f'#{test} {cnt}')