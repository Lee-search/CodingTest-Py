N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
answer = 0

if False:
    used = 0
    for _ in range(M):
        if used < K:
            answer += nums[N - 1]
            used += 1
        else:
            answer += nums[N - 2]
            used = 0

first = nums[N - 1]
second = nums[N - 2]

count = (M // (K + 1)) * K
count += M % (K + 1)

answer += first * count
answer += second * (M - count)

print(answer)