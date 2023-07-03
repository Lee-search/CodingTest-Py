t = int(input())
for test_case in range(1, t + 1):
    # 맵 사이즈, 분사력
    n, m = map(int, input().split())

    plain = []
    for _ in range(n):
        plain.append(list(map(int, input().split())))

    def check_plus(r: int, c: int):
        result = plain[r][c]

        for i in range(1, m):   # UP
            now_r = r - i
            if now_r < 0:
                break
            result += plain[now_r][c]

        for i in range(1, m):   # DOWN
            now_r = r + i
            if now_r >= n:
                break
            result += plain[now_r][c]

        for i in range(1, m):   # LEFT
            now_c = c - i
            if now_c < 0:
                break
            result += plain[r][now_c]

        for i in range(1, m):   # RIGHT
            now_c = c + i
            if now_c >= n:
                break
            result += plain[r][now_c]

        return result


    def check_x(r: int, c: int):
        result = plain[r][c]

        for i in range(1, m):   # 11
            now_r, now_c = r - i, c - i
            if now_r < 0 or now_c < 0:
                break
            result += plain[now_r][now_c]

        for i in range(1, m):   # 1
            now_r, now_c = r - i, c + i
            if now_r < 0 or now_c >= n:
                break
            result += plain[now_r][now_c]

        for i in range(1, m):   # 5
            now_r, now_c = r + i, c + i
            if now_r >= n or now_c >= n:
                break
            result += plain[now_r][now_c]

        for i in range(1, m):   # 7
            now_r, now_c = r + i, c - i
            if now_r >= n or now_c < 0:
                break
            result += plain[now_r][now_c]

        return result

    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, check_plus(i, j), check_x(i, j))

    print(f'#{test_case} {answer}')