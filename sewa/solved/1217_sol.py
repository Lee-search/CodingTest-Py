for test in range(1, 11):
    N = int(input())
    a, b = map(int, input().split())

    def mu(i: int) -> int:
        if i == b:
            return 1
        return a * mu(i + 1)

    print(f'#{test} {mu(0)}')