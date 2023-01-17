from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        # 큐에서 원소 하나 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 방문하지 않은 인접노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드의 방문된 정보를 포현
visited = [False] * 9

bfs(graph, 1, visited)