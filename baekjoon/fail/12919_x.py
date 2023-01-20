# https://www.acmicpc.net/problem/12919
# S -> T 로 BFS, 시간초과 -> S, T 위치 변경 후 클리어

s = list(input())
t = list(input())

def dfs(s: list):
    if len(s) == len(t):
        if s == t:
            print(1)
            exit()
        else:
            return

    # 1.
    s.append('A')
    dfs(s)
    s.pop()

    # 2.
    s.append('B')
    s.reverse()
    dfs(s)
    s.reverse()
    s.pop()

dfs(s)
print(0)