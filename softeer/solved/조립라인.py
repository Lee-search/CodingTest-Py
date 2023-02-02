# https://softeer.ai/practice/info.do?idx=1&eid=403
# 조립라인: DP

import sys
input = sys.stdin.readline

n = int(input())
line = [[0, 0, 0, 0] for _ in range(n)]
# 0 ~ n - 2
for i in range(n - 1):
    # 0: A_i, 1: B_i, 2: A->B, 3: B->A
    line[i] = list(map(int, input().split()))
# n - 1
line[n - 1] = list(map(int, input().split()))

# A와 B에서 시작하는 DP 테이블 생성
dp = [[0, 0] for _ in range(n)]
dp[0][0], dp[0][1] = line[0][0], line[0][1]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0] + line[i][0], dp[i - 1][1] + line[i - 1][3] + line[i][0])
    dp[i][1] = min(dp[i - 1][1] + line[i][1], dp[i - 1][0] + line[i - 1][2] + line[i][1])

print(min(dp[n - 1]))