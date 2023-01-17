# N 개의 동영상 / Q 개의 질문
N, Q = map(int, input().split())
graph = []
for _ in range(N - 1):
    graph.append(tuple(map(int, input().split())))
quest = []
for _ in range(Q):
    quest.append(tuple(map(int, input().split())))

