n = int(input())
fears = list(map(int, input().split()))
fears.sort(reverse=True)

count = 0
i = fears[0]
while i <= len(fears):
    i += i - 1
    count += 1

print(count)