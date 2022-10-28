def brute(n: int) -> list:
    # N, E, S, W
    d = [0, 1, 2, 3]
    sols = []

    for i in range(2 ** n):
        b = bin(i)[2:]

        if len(b) <= n:
            b = '0' * (n - len(b)) + b
        sols.append(list(map(int, b)))

    return sols

print(brute(6))
