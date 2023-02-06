import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
start_x, start_y = map(int, input().split())
stores = [list(map(int, input().split())) for _ in range(n)]   # 편의점 위치 받기
dest_x, dest_y = map(int, input().split())

visited = [False for _ in range()]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
