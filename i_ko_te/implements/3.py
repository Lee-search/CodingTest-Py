pos = input()
r = int(pos[1])
c = ord(pos[0]) - ord('a') + 1

# 나이트 이동 경우의 수, 8가지
dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

count = 0
for d in range(8):
    nr = r + dr[d]
    nc = c + dc[d]

    if 0 < nr <= 8 and 0 < nc <= 8:
        count += 1
print(count)

## Opi
steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
count = 0
for step in steps:
    nr = r + step[0]
    nc = c + step[1]

    if 1 <= nr <= 8 and 1 <= nc <= 8:
        count += 1
print(count)