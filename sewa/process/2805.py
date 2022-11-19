T = int(input())
for test in range(1, T + 1):
    N = int(input())
    plain = []
    for _ in range(N):
        plain.append(list(map(int, input())))

    value = 0
    for i, r in enumerate(range(N)):
        if i <= N//2:   c = i
        else:   c = N - 1 - i
        print(plain[r][N//2 - c:N//2 + c + 1])
        value += sum(plain[r][N//2 - c:N//2 + c + 1])
    print(f'#{test} {value}')