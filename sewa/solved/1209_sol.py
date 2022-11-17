for n in range(1, 11):
    N = int(input())
    plain = []

    for _ in range(100):
        plain.append(list(map(int, input().split())))

    biggest = 0
    x_3, x_4 = 0, 0

    for i in range(100):
        x_1, x_2 = 0, 0
        x_3 += plain[i][i]
        x_4 += plain[i][99 - i]
        for j in range(100):
            x_1 += plain[i][j]
            x_2 += plain[j][i]
        biggest = max(biggest, x_1, x_2)

    print('#' + str(i) + ' ' + str(max(biggest, x_3, x_4)))
    