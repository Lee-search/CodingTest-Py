for N in range(1, 11):
    n = int(input())

    plain_1 = []
    plain_2 = []
    for _ in range(8):
        plain_1.append(input())

    for i in range(8):
        s = ""
        for j in range(8):
            s += plain_1[j][i]
        plain_2.append(s)

    cnt = 0
    for i in range(8 - n  + 1):
        for j in range(8 - n  + 1):
            if plain_1[i][j:j + n // 2] == plain_1[i][j + n // 2:j + n][::-1]:
                cnt += 1

            if plain_2[i][j:j + n // 2] == plain_2[i][j + n // 2:j + n][::-1]:
                cnt += 1

    print(f"#{N} {cnt * 2}")