h, w = map(int, input().split())
heights = list(map(int, input().split()))
#blocks = [[0] * w for _ in range(h)]

from collections import defaultdict
dic = defaultdict(list)

for c in range(w):
    for r in range(h - 1, h - 1 - heights[c], -1):
        dic[r].append(c)

for r in dic.keys():
    if len(dic[r]) <= 1:
        continue

    for c in dic[r]:

