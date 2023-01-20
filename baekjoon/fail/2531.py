n, d, k, c = map(int, input().split())
sushi = [ int(input()) for _ in range(n) ]

answer = 0
i = 0
while True:
    front = i
    back = i + k
    if back == n + 1:
        break

    now = set(sushi[front:back])
    answer = max(answer, len(now))
    if c not in now:
        answer += 1

    i += 1
print(answer)