# https://www.acmicpc.net/problem/5972
# 택배: 다익스트라 이용

# n: 헛간의 수, m: 길의 수
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))   # 비용, 도착지점
    graph[b].append((cost, a))

INF = int(1e9)
cost_array = [INF] * (n + 1)

from heapq import heappop, heappush

def dijkstra(start):
    queue = []  # 우선순위 큐
    # 출발 -> 출발은 가중치 0
    heappush(queue, (0, start))
    cost_array[start] = 0

    while queue:
        # 가중치, 현재위치
        cost, now = heappop(queue)
        
        # 이미 처리된 노드인 경우
        if cost_array[now] < cost:
            continue

        for i_cost, i_next in graph[now]:
            next_cost = cost + i_cost
            # 다른 경로 가중치 < 기존 경로 가중치
            if next_cost < cost_array[i_next]:
                cost_array[i_next] = next_cost
                heappush(queue, (next_cost, i_next))

dijkstra(1)
print(cost_array[n])
