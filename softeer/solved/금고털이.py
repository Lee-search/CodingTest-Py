import sys
input = sys.stdin.readline
# 배낭의 무게, 귀금속 종류
W, N = map(int, input().split())

bank = [0] * (N + 1)
for _ in range(N):
    amount, value = map(int, input().split())
    # 가치 -> 갯수
    bank[value] += amount

answer = 0
for val in range(len(bank) - 1, -1, -1):
    if bank[val] == 0:
        continue

    # 가방의 용량 부족한 경우
    if W < bank[val]:
        answer += val * W
        break

    # 가방의 용량 충분한 경우
    answer += val * bank[val]
    W -= bank[val]

print(answer)