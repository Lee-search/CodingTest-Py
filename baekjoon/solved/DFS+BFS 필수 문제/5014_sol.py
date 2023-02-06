# https://www.acmicpc.net/problem/5014
# 스타트링크: BFS 기본예제

import sys
input = sys.stdin.readline
from collections import deque

# 최대 높이, 출발지점, 도착지점, 위로 U칸, 아래로 D칸
F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)

def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        pos, cnt = q.popleft()
        if pos == end:
            print(cnt)
            exit()

        moved = [pos + U, pos - D]
        for i in moved:
            if 0 < i <= F and not visited[i]:
                q.append((i, cnt + 1))
                visited[i] = True

bfs(S, G)
print("use the stairs")