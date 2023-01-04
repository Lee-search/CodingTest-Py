# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque

def solution(n, computers):
    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True

        while queue:
            current = queue.popleft()
            #print(current)
            for i in range(n):
                if i != current and computers[current][i] and not visited[i]:
                    queue.append(i)
                    visited[i] = True


    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))