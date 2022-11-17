N, M = map(int, input().split())
plain = []

for i in range(N):
    line = list(map(int, input().split()))
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

import pprint as pp
print(pp.pprint(cam_5(2,2)))

# MAIN
while True:
    f_count, f_list = find_fish()

    if f_count == 0:    # 한마리도 없음
        print(S.moved, S.size, S.row, S.col)
        break
    if f_count == 1:    # 한마리 있음 -> 먹을 수 있으면 이동, 없으면 종료
        print(S.moved, S.size, S.row, S.col)
        f_row, f_col = f_list[0][0], f_list[0][1]
        dist = get_distance(f_row, f_col)
        if dist >= 0:   # Eatable
            S.moved += dist
            S.counter += 1
            S.set_size()
            plain[S.row][S.col] = 0   # Away
            S.row, S.col = f_row, f_col
            plain[S.row][S.col] = 9   # EAT
        else:
            break

    if f_count >= 2:    # 두마리 이상 -> 제일 가까이 있는 것 이동, 없으면 종료
        print(S.moved, S.size, S.row, S.col)
        min_d = 999
        r, c, s = -1, -1, -1

        for i in range(len(f_list)):
            dist = get_distance(f_list[i][0], f_list[i][1])
            if dist != -1 and dist < min_d:    # 더 가까우면
                min_d = dist
                (r, c, s) = f_list[i]

        if min_d != 999 and (r, c, s) != (-1, -1, -1):
            S.moved += min_d
            S.counter += 1
            S.set_size()
            plain[S.row][S.col] = 0  # Away
            S.row, S.col = r, c
            plain[S.row][S.col] = 9  # EAT
        else:
            break

print(S.moved)