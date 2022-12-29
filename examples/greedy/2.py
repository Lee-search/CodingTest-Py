N, M = map(int, input().split())
plain = [ list(map(int, input().split())) for _ in range(N) ]

answer = 0
for i in range(N):
    #answer = max(answer, sorted(plain[i])[0])
    answer = max(answer, min(plain[i]))

print(answer)
