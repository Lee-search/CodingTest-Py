for test in range(1, 11):
    N = int(input())

    plain = []
    for _ in range(8):
        plain.append(list(input()))
    plain_reversed = []
    for c in range(8):
        plain_reversed.append([plain[r][c] for r in range(8)])


    cnt = 0
    for r in range(8):
        for c in range(8 - N + 1):
            if N % 2 == 1:  k = 1
            else: k = 0

            if plain[r][c:c + N // 2] == list(reversed(plain[r][c+ N // 2 + k:c + N])):
                cnt += 1
            if plain_reversed[r][c:c + N // 2] == list(reversed(plain_reversed[r][c+ N // 2 + k:c + N])):
                cnt += 1

    print(f"#{test} {cnt}")