# https://softeer.ai/practice/info.do?idx=1&eid=407
# 바이러스/난이도 2: 점화식 구하기
import sys
k, p, n = map(int, sys.stdin.readline().split())
# ** 연산자 대신 pow 쓰기
print(k * pow(p, n, 1000000007) % 1000000007)