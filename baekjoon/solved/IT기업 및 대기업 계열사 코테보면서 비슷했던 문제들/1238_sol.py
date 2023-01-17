# https://www.acmicpc.net/problem/1238
# 파티: 다익스트라 알고리즘 이용한 문제

import heapq

INF = int(1e9)
# 출발지, 도착지 -> 도착지까지의 비용 리턴
def dijkstra(start, dest):
    cost_array = [INF for _ in range(n + 1)]

    heap = []
    # 시작노드의 가중치, 위치 추가
    cost_array[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        # 이미 처리된 노드이면 continue
        if cost_array[now_node] < now_cost:
            continue

        # 다음 노드에 대해 코스트의 최소값 반영
        for next_node, next_cost in graph[now_node]:
            cost = now_cost + next_cost
            if cost < cost_array[next_node]:
                cost_array[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    # 다녀간 노드 중 목적지의 가중치 리턴
    return cost_array[dest]

# n명의 학생들, x번 마을에서 축제, m은 간선의 갯수
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    # start -> end 까지 걸리는 비용
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

answer = 0
for i in range(1, n + 1):
    # 제자리에서 이동하는 경우 제외, 항상 0
    if i == x:
        continue

    # 갔다가 돌아오는 최소 비용 계산
    total = dijkstra(i, x) + dijkstra(x, i)
    answer = max(answer, total)
print(answer)
