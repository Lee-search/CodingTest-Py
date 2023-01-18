# https://www.acmicpc.net/problem/1253
# 좋다: 정렬, 이중 포인터 사용

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
for i in range(n):
    target = numbers[i]
    others = numbers[:i] + numbers[i + 1:]
    
    # 앞, 뒤부터 시작하는 포인터
    front, back = 0, len(others) - 1

    while front < back:
        t = others[front] + others[back]
        if t == target:
            count += 1
            break
        # 타겟보다 작으면 front 이동시켜서 더 커져야함
        if t < target:
            front += 1
        else:
            back -= 1

print(count)