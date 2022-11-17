from collections import deque

T = int(input())
for test in range(1, T + 1):
    q = deque()
    for i in range(8):
        row = list(input())
        for j in range(8):
            if row[j] == 'O':
                q.append((i, j))

    if len(q) != 8:
        print(f'#{test} no')
        continue

    row_list = list()
    col_list = list()
    while q != deque():
        (r, c) = q.popleft()
        row_list.append(r)
        col_list.append(c)

    # print(row_list, col_list)
    if sorted(row_list) != list(range(0, 8)) or sorted(col_list) != list(range(0, 8)):
        print(f'#{test} no')
        continue

    print(f'#{test} yes')