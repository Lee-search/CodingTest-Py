# https://www.acmicpc.net/problem/14503
# 로봇 청소기: 구현, 시뮬레이션

N, M = list(map(int, input().split()))  # 세로, 가로
r, c, d = list(map(int, input().split()))   # 행, 열, 방향

import sys
input = sys.stdin.readline

plain = []
for _ in range(N):
    plain.append(list(map(int, input().split())))

cleand= 0   # 청소횟수

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def watch_left(d: int): # 회전
    return (d + 3) % 4
    #if d == 0: return 3
    #elif d == 1: return 0
    #elif d == 2: return 1
    #elif d == 3: return 2

def move_front(r: int, c: int, d: int):
    r, c = r + dr[d], c + dc[d]
    return r, c

def move_back(r: int, c: int, d: int):
    d = watch_left(watch_left(d))
    return move_front(r, c, d)

while True:
    #print((r, c, d))
    if plain[r][c] == 0:
        plain[r][c] = -1 # 청소
        cleand += 1

    # r, c, d, plain[r][c]
    for _ in range(4):
        d = watch_left(d)   # 회전
        nr, nc = move_front(r, c, d)
        #if nr < 0 or nr >= N or nc < 0 or nc >= M:  # Out-of-range
        if plain[nr][nc] == 1 or plain[nr][nc] == -1:
            continue

        if plain[nr][nc] == 0:
            r, c = nr, nc   # Move
            break

    if plain[r][c] == 0:
        continue

    nr, nc = move_back(r, c, d)
    #if nr < 0 or nr >= N or nc < 0 or nc >= M:  # Out-of-range, 벽인 경우
    if plain[nr][nc] == 1:
        break
    r, c = nr, nc   # Move

print(cleand)


