import sys
input = sys.stdin.readline

w, n = map(int, input().split())
bank = [(0,0)] * n
for i in range(n):
    # 양, 1키로당 가치
    amount, value = map(int, input().split())
    bank[i] = amount, value    # 양, 가치 순
# 가치를 기준으로 정렬
bank.sort(key=lambda x: x[1], reverse=True)

sum = 0
start = 0
for a, val in bank:
    # 배낭보다 금고의 남은 양이 더 많은 경우, 가능한만큼 담고 종료
    if start + a > w:
        for j in range(start, w):
            sum += val
        break
    # 해당 보석을 배낭에 충분히 담을 수 있음
    else:
        for j in range(start, a):
            sum += val
        start += a

print(sum)