import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 방문 체크 리스트
visited = [False] * (n + 1)
# 최단거리 테이블
distance = [INF] * (n + 1)

for _ in range(m):
    # a -> b, cost
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지않은 노드 중에서 가장 방문 거리가 짧은 노드 리턴
def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for b, cost in graph[start]:
        distance[b] = cost

    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for b, cost in graph[now]:
            cost = distance[now] + cost
            if cost < distance[b]:
                distance[b] = cost

# 다익스트라 수행
dijkstra(start)

# 각 노드의 최단거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

