n, k  = map(int, input().split())
product = []
for _ in range(n):
    product.append(list(map(int, input().split())))

product.sort(key=lambda x : x[0])

