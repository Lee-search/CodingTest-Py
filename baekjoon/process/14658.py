n, m, l, k = map(int, input().split())
stars = list(tuple(map(int, input().split())) for _ in range(k))

plain = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        # 트램펄린 배치

