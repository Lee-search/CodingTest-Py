import sys
input = sys.stdin.readline

N = int(input())
works = []
for i in range(1, N + 1):
    t, p = map(int, input().split())
    if (N - i - t) >= 0:    # 할 수 있는 일만 추리기
        works.append((t, p))

MAX = 0


print(MAX)

def get_job(n: int, ):
    for i in range(len(works)):  # i 일차 작업을 무조건 수용
        s = 0
        for j in range(0, i):
            t, p = works[j]
            if j + t < i:
                s += p
                j += t
        s = works[i][1]
        for j in range(i + 1, len(works)):
            t, p = works[j]
            if j + t < N:
                s += p
                j += t
        MAX = max(MAX, s)