from collections import deque

def solution(number, k):
    stack = []

    for num in str(number):
        if not stack:
            stack.append(num)
        if k > 1:
            for each in stack:
                if int(each) < int(num):
                    stack.remove(each)
                    stack.append(num)
                    k -= 1
    return "".join(stack)

print(solution(12321, 2))