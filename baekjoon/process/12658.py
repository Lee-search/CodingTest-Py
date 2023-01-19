# N 가로길이, M 세로길이, L 트램펄린 한 변의 길이, K 별똥별의 수
n, m, l, k = map(int, input().split())
plain = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x, y = map(int, input().split())
    plain[x][y] = 1

for i in range(n):
    for j in range(m):
        plain[]