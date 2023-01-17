N = int(input())
command = input().split()

# L, R, U, D
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
r, c = 1, 1

for i in command:
    if i == 'L':    d = 0
    elif i == 'R':  d = 1
    elif i == 'U':  d = 2
    else:           d = 3

    nr = r + dr[d]
    nc = c + dc[d]
    if 0 < nr < N and 0 < nc < N:
        r, c = nr, nc

print(r, c)
