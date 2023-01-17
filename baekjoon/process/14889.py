N = int(input())
stats = []
for _ in range(N):
    stats.append(list(map(int, input().split())))
persons = [False] * N

min_val = 100 * (N / 2)

def others(p: list) -> int:
    s = 0
    for i in p:
        s += stats[i]
    return s

others([0,1,2])

def DFS(n: int, i: int):
    global min_val

    if i == N:
        min_val = min(min_val, n)
    else:
        if not persons[i]:
            persons[i] = True
            n = n + stats[i][0]
            DFS(n, i + 1)
            persons[i] = False
