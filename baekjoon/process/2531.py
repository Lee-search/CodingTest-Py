n, d, k, c = map(int, input().split())
sushi = [ int(input()) for _ in range(n) ]
sushi.extend(sushi)

answer = 0

left = 0
right = k - 1

while True:
    if front == i + 1:
        break

    now = set(sushi[front:back])
    answer = max(answer, len(now))
    if c not in now:
        answer += 1
print(answer)