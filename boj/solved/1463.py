n = int(input())

d = [0] * (1000000 + 1)
for i in range(2, n + 1):
    # -1을 할 수 없는 경우는 없음
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])