# https://www.acmicpc.net/problem/2493
# 탑: 완전탐색으로 풀었으나 시간초과

n = int(input())
top_list = list(map(int, input().split()))
answer = [0] * n

# 뒤에서 앞으로 탐색
for i in range(n - 1, -1, -1):
    target = top_list[i]
    for j in range(i - 1, -1, -1):
        if top_list[j] >= target:
            answer[i] = j + 1
            break

print(' '.join(str(s) for s in answer))