import sys
input = sys.stdin.readline

N, M = map(int, input().split())
plain = []
for _ in range(N):
    plain.append(list(map(int, input().split())))
    
origin = plain  # 원본 저장

def find_camera() -> list:
    cam_list = []

    for i in range(N):
        for j in range(M):
            if plain[i][j] in range(1,6):
                cam_list.append((plain[i][j], i, j))
    return cam_list

cams = find_camera() # -> [(종류, 좌표)]

def getZArea():
    sum = 0

    for i in range(N):
        for j in range(M):
            if plain[i][j] == 0:
                sum += 1
    return sum

# 북,동,남,서 -> 0,1,2,3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def cam_1(r:int, c: int, d: int):  # r, c: 카메라 좌표
    p = plain
    while True:
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr > N - 1 or nc < 0 or nc > M - 1:    # 맵 밖으로 나감
            break
            
        r, c = nr, nc   # Move
        if p[r][c] == 0:    # 0 -> -1
            p[r][c] = -1
        elif p[r][c] == 6:  # 벽 -> break
            break
        else:   # 카메라 or -1 -> pass
            continue
    return p

total = []

def makeSolutions(c: int) -> list:
    solutions = []
    for _ in range(c):
        temp = []
        for i in range(4):
                temp.append(j)
        solutions.append(temp)
    return solutions


for c in cams:
    c_no, cx, cy = c[0], c[1], c[2]




    for d in range(4):  # 북, 동, 남, 서
        cam_1(c_x, c_y, d)
        
        
print(plain)
print(getZArea())