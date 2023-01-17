# https://www.acmicpc.net/problem/14888
# 브루트포스 알고리즘, 백트래킹

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())

max_val = -10 ** 9
min_val = 10 ** 9

# idea from: https://data-flower.tistory.com/72
def DFS(n: int, i: int):
    global plus, minus, mult, div, max_val, min_val

    if i == N:
        max_val = max(n, max_val)
        min_val = min(n, min_val)
    else:
        if plus > 0:
            plus -= 1
            DFS(n + nums[i], i + 1)
            plus += 1
        if minus > 0:
            minus -= 1
            DFS(n - nums[i], i + 1)
            minus += 1
        if mult > 0:
            mult -= 1
            DFS(n * nums[i], i + 1)
            mult += 1
        if div > 0:
            div -= 1
            DFS(int(n / nums[i]), i + 1)
            div += 1

DFS(nums[0], 1)
print(max_val)
print(min_val)