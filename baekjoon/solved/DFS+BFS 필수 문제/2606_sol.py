# https://www.acmicpc.net/problem/2606
# 바이러스: BFS

n = int(input())
m = int(input())

rel_table = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    rel_table[a].append(b)
    rel_table[b].append(a)

from collections import deque
visited = [False] * (n + 1)
#print(visited)
def bfs(start = 1):
    q = deque()
    q.append(start)
    visited[start] = True
    virus = 0

    while q:
        v = q.popleft()
        for i in rel_table[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                virus += 1

    print(virus)

bfs(1)