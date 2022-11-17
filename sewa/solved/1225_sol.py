from collections import deque

for _ in range(10):
    test = int(input())
    q = deque(map(int, input().split()))

    flag = False
    while not flag:
        for i in range(1, 6):
            num = q.popleft() - i
            if num <= 0:
                flag = True
                q.append(0)
                break
            q.append(num)

    print('#' + str(test) +  ' ' + ' '.join([str(q[i]) for i in range(8)]))