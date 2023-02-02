# https://softeer.ai/practice/info.do?idx=1&eid=390
# 스택으로 풀었으나 오답

import sys
input = sys.stdin.readline

n = int(input())
bridge = list(map(int, input().split()))
stack = []

answer = 0
for i in range(n):
    #print(stack)
    while stack:
        if stack[-1] < bridge[i]:
            break
        else:
            answer = max(answer, len(stack))
            stack.clear()
    stack.append(bridge[i])

# 반복문 종료 후 마지막 인자에 대해서도 비교
answer = max(answer, len(stack))
print(answer)