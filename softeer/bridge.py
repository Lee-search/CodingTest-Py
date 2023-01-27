n = int(input())
bridge = list(map(int, input().split()))

dp = [1] * n

for i in range(len(bridge) - 1):    # 마지막 칸 제외
    next = i + 1
    while True:
        if next >= n or bridge[next - 1] >= bridge[next]:
            break
        else:
            dp[i] += 1
            next += 1

#print(dp)
print(max(dp))