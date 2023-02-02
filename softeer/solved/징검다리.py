# https://softeer.ai/practice/info.do?idx=1&eid=390
# 징검다리: DP, 각 위치에서 건널 수 있는 최대치를 구함

import sys
input = sys.stdin.readline

n = int(input())
bridge = list(map(int, input().split()))

# 모든 위치에서 최소 한 칸은 건널 수 있음
answer = [1] * n

for i in range(1, n):
    for j in range(i):
        if bridge[j] < bridge[i]:
            answer[i] = max(answer[i], answer[j] + 1)

print(max(answer))