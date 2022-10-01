# Input
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# Output - 10

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)
# [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

# 상하좌우 이동
# mover = [[-1, 0], [1, 0], [0, -1], [0, 1]]

from collections import deque

def bfs(x, y):
    #if x <= -1 or x >= n or y <= -1 or y >= m:
    #    return 0

    count = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        v = queue.popleft() # x, y
        p_x = v[0]
        p_y = v[1]
        graph[p_x][p_y] = 0 # 방문처리 1 -> 0

        if p_x == n - 1 and p_y == m - 1:
            print(count)
            break

        if graph[p_x - 1][p_y] == 1:
            queue.append((p_x - 1, p_y))

        if graph[p_x + 1][p_y] == 1:
            queue.append((p_x + 1, p_y))

        if graph[p_x][p_y - 1] == 1:
            queue.append((p_x, p_y - 1))

        if graph[p_x][p_y + 1] == 1:
            queue.append((p_x, p_y + 1))

        count += 1

bfs(n,m)