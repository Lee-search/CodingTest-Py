def dfs(computers, v, visited):
    visited[v] = True

    for next in range(len(computers)):
        if computers[v][next]:
            if not visited[next]:
                dfs(computers, next, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for v in range(n):
        if not visited[v]:
            dfs(computers, v, visited)
            answer += 1

    return answer