N, M = map(int, input().split())
plain = []
cam_list = []

for i in range(N):
    line = list(map(int, input().split()))
    cam_list.extend([(line[j], i, j) for j in range(len(line)) if line[j] in range(1, 6)])
    plain.append(line)

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

import copy
def cam_1(r:int, c:int):
    p_list = []
    for i in range(4):
        tr, tc = r, c
        p = copy.deepcopy(plain)
        while True:
            nr = tr + dr[i]
            nc = tc + dc[i]
            print(nr, nc)

            if nr < 0 or nr >= N or nc < 0 or nc >= M or p[nr][nc] == 6:
                break
            p[nr][nc] = -1
            tr, tc = nr, nc
        p_list.append(p)
    return p_list

def cam_2(r: int, c: int):
    p_list = cam_1(r, c)
    new_list = []
    for k in range(2):
        p = copy.deepcopy(p_list[k])
        for i in range(N):
            for j in range(M):
                if p_list[k + 2][i][j] == -1:
                    p[i][j] = -1
        new_list.append(p)
    return new_list

def cam_3(r: int, c: int):
    p_list = cam_1(r, c) * 2
    new_list = []
    for k in range(4):
        p = copy.deepcopy(p_list[k])
        for i in range(N):
            for j in range(M):
                if p_list[(k + 1) % 4][i][j] == -1:
                    p[i][j] = -1
        new_list.append(p)
    return new_list

def cam_4(r: int, c: int):
    p_list = cam_2(r, c) * 2
    cam1_list = cam_1(r,c)
    new_list = []
    for k in range(4):
        p = copy.deepcopy(p_list[k])
        for i in range(N):
            for j in range(M):
                if cam1_list[(k + 1) % 4][i][j] == -1:
                    p[i][j] = -1
        new_list.append(p)
    return new_list

def cam_5(r: int, c: int):
    p_list = cam_2(r, c)
    new_list = []
    p = copy.deepcopy(p_list[0])
    for i in range(N):
        for j in range(M):
            if p_list[1][i][j] == -1:
                p[i][j] = -1
    new_list.append(p)
    return new_list

def select_cam(n:int, r:int, c:int):
    if n == 1:
        return cam_1(r, c)
    elif n == 2:
        return cam_2(r, c)
    elif n == 3:
        return cam_3(r, c)
    elif n == 4:
        return cam_4(r, c)
    else:
        return cam_5(r, c)

## MAIN
plains = []
for (n, r, c) in cam_list:
    new_plains = select_cam(n, r, c)
    if plains == []:
        plains = new_plains
        continue

    for p in plains:
        for i in range(N):
            for j in range(M):
                if new_plains[i][j] == -1:
                    p[i][j] = -1




