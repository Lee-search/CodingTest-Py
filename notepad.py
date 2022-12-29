lista = [[1,2,3,4,5],[6,7,8,9,0]]

print(lista[0][1:])

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move(r: int, c: int, d: int):
    nr = r + dr[d]
    nc = c + dc[d]
    if (0 <= nr < n and 0 <= nc < m) and plain[nr][nc] == 1:
        r, c = nr, nc

    return (r, c)


from collections import deque

queue = deque((0, 0))

while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr, nc = move(r, c, i)
        if (nr, nc) not in queue:
            queue.append((nr, nc))
