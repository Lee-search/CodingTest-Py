# https://www.acmicpc.net/problem/14500
# 테트로미노: 구현, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
plain = []
for _ in range(N):
    plain.append(list(map(int, input().split())))

# r: Row, c: Column
def I_mino(r: int, c:int) -> list:  # 2개
    ms = []
    if c + 3 <= M - 1:
        ms.append([(r, j) for j in range(c, c + 4)])
    if r + 3 <= N - 1:
        ms.append([(i, c) for i in range(r, r + 4) ])
    return ms

def O_mino(r: int, c:int) -> list:  # 1개
    ms = []
    if r + 1 <= N - 1 and c + 1 <= M - 1:
        ms.append([(i, j) for i in range(r, r + 2) for j in range(c, c + 2)])
    return ms

def L_mino(r: int, c:int) -> list:  # 8개
    ms = []
    if r + 2 <= N - 1 and c + 1 <= M - 1:
         ms.append([(r, c), (r + 1, c), (r + 2, c), (r + 2, c + 1)])
    if r + 1 <= N - 1 and c + 2 <= M - 1:
        ms.append([(r, c), (r, c + 1), (r, c + 2), (r + 1, c)])
    if r + 2 <= N - 1 and c - 1 >= 0:
        ms.append([(r, c - 1), (r, c), (r + 1, c), (r + 2, c)])
    if r - 1 >= 0 and c - 2 >= 0:
        ms.append([(r - 1, c), (r, c), (r, c - 1), (r, c - 2)])
    if r - 2 >= 0 and c - 1 >= 0:
        ms.append([(r, c), (r, c - 1), (r - 1, c), (r - 2, c)])
    if r + 1 <= N - 1 and c - 2 >= 0:
        ms.append([(r, c), (r + 1, c), (r, c - 1), (r, c - 2)])
    if r + 2 <= N - 1 and c + 1 <= M - 1:
        ms.append([(r, c), (r, c + 1), (r + 1, c), (r + 2, c)])
    if r - 1 >= 0 and c + 2<= M - 1:
        ms.append(([(r, c), (r - 1, c), (r, c + 1), (r, c + 2)]))

    return ms

def S_mino(r: int, c:int) -> list:  # 4개
    ms = []
    if r + 2 <= N - 1 and c + 1 <= M - 1:
        ms.append([(r, c), (r + 1, c), (r + 1, c + 1), (r + 2, c + 1)])
    if r + 1 <= N - 1 and c - 2 >= 0:
        ms.append([(r, c), (r, c - 1), (r + 1, c - 1), (r + 1, c - 2)])
    if r + 2 <= N - 1 and c - 1 >= 0:
        ms.append([(r, c), (r + 1, c), (r + 1, c - 1), (r + 2, c- 1)])
    if r + 1 <= N - 1 and c + 2 <= M - 1:
        ms.append([(r, c), (r, c + 1), (r + 1, c + 1), (r + 1, c + 2)])
    return ms

def T_mino(r: int, c:int) -> list:  # 4개
    ms = []
    if r + 1 <= N - 1 and c + 2 <= M - 1:
        ms.append([(r, c), (r, c + 1), (r, c + 2), (r + 1, c + 1)])
    if r + 2 <= N - 1 and c - 1 >= 0:
        ms.append([(r, c), (r + 1, c), (r + 2, c), (r + 1, c - 1)])
    if r - 1 >= 0 and c - 2 >= 0:
        ms.append([(r, c), (r, c - 1), (r - 1, c - 1), (r, c - 2)])
    if r - 2 >= 0 and c + 1 <= M - 1:
        ms.append([(r, c), (r - 1, c), (r - 2, c), (r - 1, c + 1)])
    return ms

MAX = 0

for i in range(N):
    for j in range(M):
        for b1, b2, b3, b4 in I_mino(i, j): # 4개의 블록 리턴
            MAX = max(MAX, plain[b1[0]][b1[1]] + plain[b2[0]][b2[1]] + plain[b3[0]][b3[1]] + plain[b4[0]][b4[1]])

        for (b1, b2, b3, b4) in O_mino(i, j):
            MAX = max(MAX, plain[b1[0]][b1[1]] + plain[b2[0]][b2[1]] + plain[b3[0]][b3[1]] + plain[b4[0]][b4[1]])

        for (b1, b2, b3, b4) in L_mino(i, j):
            MAX = max(MAX, plain[b1[0]][b1[1]] + plain[b2[0]][b2[1]] + plain[b3[0]][b3[1]] + plain[b4[0]][b4[1]])

        for (b1, b2, b3, b4) in S_mino(i, j):
            MAX = max(MAX, plain[b1[0]][b1[1]] + plain[b2[0]][b2[1]] + plain[b3[0]][b3[1]] + plain[b4[0]][b4[1]])

        for (b1, b2, b3, b4) in T_mino(i, j):
            MAX = max(MAX, plain[b1[0]][b1[1]] + plain[b2[0]][b2[1]] + plain[b3[0]][b3[1]] + plain[b4[0]][b4[1]])

print(MAX)