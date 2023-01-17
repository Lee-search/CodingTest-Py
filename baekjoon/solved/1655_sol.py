# https://www.acmicpc.net/problem/1655
# 가운데를 말해요: 우선순위 큐

import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        # 왼쪽은 최대힙으로 구성
        heapq.heappush(left_heap, -num)
    else:
        # 오른쪽은 최소힙으로 구성
        heapq.heappush(right_heap, num)

    if right_heap and -left_heap[0] > right_heap[0]:
        l, r = -heapq.heappop(left_heap), heapq.heappop(right_heap)
        # 두 힙 사이의 대소관계가 어긋나는 경우 스왑으로 교정
        heapq.heappush(left_heap, -r)
        heapq.heappush(right_heap, l)
        
    print(-left_heap[0])