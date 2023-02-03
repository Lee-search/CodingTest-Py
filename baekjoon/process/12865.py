import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
dp = [0] * (k + 1)
data = []

for _ in range(n):
    w, v = map(int, input().split())
    data.append((w, v))
data.sort()

# 무게가 가장 작은 것부터 넣기
for w, v, in data:
    for i in range(k, -1, -1):
        if i < w:
            break
        # 기존 값과 새로 구한 값 비교
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])