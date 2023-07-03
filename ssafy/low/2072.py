T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    answer = 0

    for i in nums:
        if i % 2 == 1:
            answer += i

    print(f'#{t} {answer}')