T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    maximum = 0

    for i in nums:
        if i > maximum:
            maximum = i

    print(f'#{t} {maximum}')