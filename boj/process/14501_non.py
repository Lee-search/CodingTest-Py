n = int(input())

jobs = []
for i in range(n):
    t, p = map(int, input().split())
    jobs.append((t, p))

pay = 0
i = 0
while i < n:
    t = jobs[i][0]
    if t <= n - i:
        pay += jobs[i][1]
    i += t

print(pay)

