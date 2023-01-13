n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

def dfs(start):
