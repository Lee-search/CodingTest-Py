n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = len(array) - 1
answer = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)

# 4 6
# 19 15 10 17