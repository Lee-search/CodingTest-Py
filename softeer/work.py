h, k, r = map(int, input().split())

worker = [[[], []] for _ in range(2 ** (h - 1) -1)]

from heapq import heappush, heappop
for _ in range(2 ** h // 2):
    # h = 1, 말단: 2^h 개
    left_node = list(map(int, input().split()))
    right_node = list(map(int, input().split()))

    solved = 0
    for day in range(r):
        # 완쪽 말단 노드
        left_que = []
        for x in left_node:
            heappush(left_que, x)

        # 오른쪽 말단 노드
        right_que = []
        for x in right_node:
            heappush(right_que, x)

        # 중간 관리자 노드
        middle_q = [[],[]]
        # 각각 업무 하나씩 상사한테 보고
        # 0: 왼쪽, 1: 오른쪽
        heappush(middle_q[0], heappop(left_que))
        heappush(middle_q[1], heappop(right_que))

        if day % 2 == 1:
            solved += heappop(middle_q[0])
        else:
            solved += heappop(middle_q[1])

print(solved)