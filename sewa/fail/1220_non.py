N = int(input())

from collections import deque

q = deque()
n_q = deque()
s_q = deque()

for i in range(N):
    line = list(map(int, input().split()))
    plain.append(line)

    for j in range(N):
        if line[j] == 1:
            q.append((i, j, line[j]))
            n_q.append((i, j))

        if line[j] == 2:
            q.append((i, j, line[j]))
            s_q.append((i, j))

cnt =0
while q != deque():
    r, c, mag = q.popleft()
    if mag == 1 and n_q != deque():
        n_q.popleft()
    if mag == 2 and s_q != deque():
        s_q.popleft()

    if mag == 1 and (r + 1 <= N - 1):
        #if (r + 1, c) in n_q:
        #    pass
        if (r + 1, c) in s_q:   # 다른 극 이면
            cnt += 1
            s_q.remove((r + 1, c))
        else:    # 0이면, 큐에 삽입
            q.append((r + 1, c, 2))
            n_q.append((r + 1, c))

    elif mag == 2 and (r - 1 >= 0):
        if (r - 1, c) in n_q:   # 다른 극 이면
            cnt += 1
            n_q.remove((r - 1, c))
        else:    # 0이면, 큐에 삽입
            q.append((r - 1, c, 2))
            n_q.append((r - 1, c))

print(cnt)






















cnt = 0
while q != deque():
    r, c, mag = q.popleft()

    if mag == 1:
        if r + 1 <= N - 1:
            r = r + 1

            if plain[r][c] == 0:
                plain[r - 1][c] = 0
                plain[r][c] = mag
                q.append((r, c, mag))

            elif plain[r][c] == mag and r + 1 <= N - 1:
                plain[r - 1][c] = 0
                plain[r + 1][c] = mag
                q.append((r + 1, c, mag))

            elif plain[r][c] == mag + 1:
                cnt += 1

    elif mag == 2:
        if r - 1 >= 0:
            r = r - 1

            if plain[r][c] == 0:
                plain[r + 1][c] = 0
                plain[r][c] = mag
                q.append((r, c, mag))

            elif plain[r][c] == mag and r - 1 >= 0:
                plain[r + 1][c] = 0
                plain[r - 1][c] = mag
                q.append((r - 1, c, mag))

            elif plain[r][c] == mag - 1:
                cnt += 1

print(cnt//2)