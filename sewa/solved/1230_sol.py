from collections import deque

for test in range(1, 11):
    int(input())
    password = list(map(int, input().split()))
    int(input())
    q = deque(input().split())


    orders = deque()
    while q != deque():
        o = q.popleft()
        if o == 'I':
            loc = int(q.popleft())
            cnt = int(q.popleft())
            password = password[:loc + 1] + [int(q.popleft()) for _ in range(cnt)] + password[loc + 1:]

        elif o == 'D':
            loc = int(q.popleft())
            cnt = int(q.popleft())
            password = password[: loc + 1] + password[loc + 1 + cnt:]
        elif o == 'A':
            cnt = int(q.popleft())
            password = password + [int(q.popleft()) for _ in range(cnt)]

    print('#' + str(test) + ' ' + ' '.join(map(str, password[1:11])))