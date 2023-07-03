def rotate(plain: list):
    rotated = []
    for c in range(n):
        line = []
        for r in range(n - 1, -1, -1):
            line.append(plain[r][c])
        rotated.append(line)

    return rotated

t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}')

    n = int(input())
    plain = [ list(map(int, input().split())) for _ in range(n) ]

    plain2str = [''] * n
    plain = rotate(plain)   # 90

    for i in range(n):
        plain2str[i] += ''.join(map(str, plain[i]))
        plain2str[i] += ' '

    plain = rotate(plain)   # 180

    for i in range(n):
        plain2str[i] += ''.join(map(str, plain[i]))
        plain2str[i] += ' '

    plain = rotate(plain)   # 270

    for i in range(n):
        plain2str[i] += ''.join(map(str, plain[i]))

    for i in range(n):
        print(plain2str[i])