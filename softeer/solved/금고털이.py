# https://softeer.ai/practice/info.do?idx=1&eid=395
# 금고털이: DP

import sys
input = sys.stdin.readline
# 배낭의 무게, 귀금속 종류
W, N = map(int, input().split())

stored = [0] * (100000 + 1)
for _ in range(N):
    amount, value = map(int, input().split())
    # 가치 -> 갯수
    stored[value] += amount

answer = 0
for val in range(len(stored) - 1, -1, -1):
    if stored[val] == 0:
        continue

    # 가방의 용량 부족한 경우
    if W < stored[val]:
        answer += val * W
        break

    # 가방의 용량 충분한 경우
    answer += val * stored[val]
    W -= stored[val]

print(answer)