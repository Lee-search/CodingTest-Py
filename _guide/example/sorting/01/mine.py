# INPUT
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(k):
    min_a = A[0]
    pos_a = 0
    for i in range(1, len(A)):
        if min_a > A[i]:
            min_a = A[i]
            pos_a = i

    max_b = B[0]
    pos_b = 0
    for i in range(1, len(B)):
        if max_b < B[i]:
            max_b = B[i]
            pos_b = i

    A[pos_a], B[pos_b] = B[pos_b], A[pos_a]

print(sum(A))