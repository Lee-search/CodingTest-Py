# https://softeer.ai/practice/info.do?idx=1&eid=584
# GBC/난이도 2: DP, 테이블을 따로 만든 뒤 각 높이에 따른 초과속도 계측
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
limits = [0] * n
datas = [0] * m

start = 0
for _ in range(n):
    loc, limit = map(int, input().split())
    # 초기화: 50m 50m/s -> limits[0:50] = 50m/s
    limits[start:start + loc] = [limit] * loc
    start += loc

start = 0
for _ in range(m):
    loc, data = map(int, input().split())
    # 초기화: 50m 50m/s -> limits[0:50] = 50m/s
    datas[start:start + loc] = [data] * loc
    start += loc

answer = 0
for i in range(100):
    over_speed = datas[i] - limits[i]
    if over_speed > answer:
        answer = over_speed

print(answer)