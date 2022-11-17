from collections import Counter
str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

N = int(input())

for test in range(1, N + 1):
    t1, t2 = input().split()
    stream = list(input().split())

    c = Counter(stream)

    print('#' + str(test))
    for i in range(10):
        for _ in range(c[str_list[i]]):
            print(str_list[i], end=' ')
    print()