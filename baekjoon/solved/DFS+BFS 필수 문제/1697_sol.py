# https://www.acmicpc.net/problem/1697
# 숨바꼭질: BFS, 리스트 바깥으로 벗어나는 경우에 대해 예외처리 필요

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [False] * (100000 + 1)

def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        pos, cnt = q.popleft()
        if pos == end:
            print(cnt)
            break

        nexts = [pos + 1, pos - 1, 2 * pos]
        for n in nexts:
            if 0 <= n <= 100000 and not visited[n]:
                q.append((n, cnt + 1))
                visited[n] = True

bfs(n, k)