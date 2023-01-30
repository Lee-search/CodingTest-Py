# https://www.acmicpc.net/problem/14719
# 빗물: 양 옆만 보지말고 전체의 최대값을 비교하기
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
# 양 끝을 뺀 중간부분에 대해 계산
for i in range(1, w - 1):
    left = heights[:i]
    right = heights[i + 1:]
    # 쌓일 수 있는 높이 - 이미 쌓여진 높이
    watering = min(max(left), max(right)) - heights[i]
    #print(watering)
    answer += watering if watering >= 0 else 0

print(answer)