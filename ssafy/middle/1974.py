def sudoku():
    plain = [list(map(int, input().split())) for _ in range(9)]

    def check_9x9(r: int, c: int):
        table = [0] * 10
        for i in range(9):  # Column Check
            if table[plain[i][c]] >= 1:
                return 0
            table[plain[i][c]] += 1

        table = [0] * 10
        for j in range(9):  # Row Check
            if table[plain[r][j]] >= 1:
                return 0
            table[plain[r][j]] += 1

        return 1

    def check_3x3(r: int, c: int):
        start_r, start_c = r // 3 * 3, c // 3 * 3
        table = [0] * 10
        for i in range(start_r, start_r + 3):
            for j in range(start_c, start_c + 3):
                if table[plain[i][j]] >= 1:
                    return 0
                table[plain[i][j]] += 1

        return 1

    for i in range(9):
        for j in range(9):
            # 굳이 매번 할 필요없이 3의 배수마다 검증하면 됨, 보완필요
            if not check_3x3(i, j):
                return 0

            if not check_9x9(i, j):
                return 0

    return 1

t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case} {sudoku()}')

