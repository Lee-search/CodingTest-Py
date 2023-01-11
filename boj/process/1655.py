from collections import deque

n = int(input())
array = deque()
for i in range(1, n + 1):
    array.append(int(input()))
    for _ in range(i):


    start = 0
    end = len(array) - 1
    mid = (start + end) // 2

    print(array[mid])