# https://softeer.ai/practice/info.do?idx=1&eid=391
# 수퍼바이러스: 점화식 구하기
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())
print(k * pow(p, n * 10, 1000000007) % 1000000007)