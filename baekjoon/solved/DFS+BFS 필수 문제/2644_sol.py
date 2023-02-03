# https://www.acmicpc.net/problem/2644
# 촌수 계산: BFS

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())    # 인수
a, b = map(int, input().split())    # 둘 사이의 촌수 계싼
m = int(input())    # 관계 수

visited = [False for _ in range(n + 1)]
# 관계 테이블 형성
rel_table = [[] for _ in range(n + 1)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    rel_table[p1].append(p2)
    rel_table[p2].append(p1)

def bfs(start):
    q = deque()
    q.append((start, 0))

    while q:
        person, depth = q.popleft()

        for i in rel_table[person]:
            if i == b:  # 찾고자 하는 사람인 경우
                print(depth + 1)
                exit()

            if not visited[i]:
                visited[i] = True
                q.append((i, depth + 1))
    print(-1)

bfs(a)