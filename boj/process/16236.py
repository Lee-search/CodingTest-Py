from collections import deque

N = int(input())
plain = []

for _ in range(N):
    plain.append(list(map(int, input().split())))

# 상어 개인정보
shark = 2
sr = -1
sc = -1
mv_count = 0

# 반복문 처음에 실행, 상어 위치 동기화 및 먹을 수 있는 생선 탐색
def find_fish() -> (int, list):
    global sr, sc
    count = 0
    fish = []
    for i in range(len(plain)):
        for j in range(len(plain[i])):
            if plain[i][j] == 9:    # Find Shark
                sr, sc = i, j
            elif 0 < plain[i][j] < shark:  # Find Eatable Fish
                #flag = get_distance(i, j)
                #if flag >= 0:  # 도달할 수 있으면
                count += 1
                fish.append((i, j))   # Row, Col
    return count, fish

# N, E, S, W
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def move(r: int, c: int, d: int) -> (int, int):
    return r + dr[d], c + dc[d]

# (r, c) 에 위치한 생선에 상어가 도달할 수 있는지 탐색
# 도달 가능하면 걸린 시간, 아니라면 -1 리턴
def get_distance(fish_r: int, fish_c: int) -> int:
    # 상어 위치 불러오기
    q = deque()
    q.append((0, sr, sc))

    while q != deque():
        count, shark_r, shark_c = q.popleft()
        if shark_r == fish_r and shark_c == fish_c: # 도달하면
            return count

        for i in range(4):
            new_sr, new_sc = move(shark_r, shark_c, i)
            if (0 <= new_sr < N and 0<= new_sc < N) and plain[new_sr][new_sc] <= shark:
                q.append((count + 1, new_sr, new_sc))
    return -1

counter = 0
def set_shark():
    global shark, counter
    if shark == counter:
        shark += 1
        counter = 0

# MAIN
while True:
    count, fish = find_fish()

    if count == 0:
        #print(mv_count, shark, sr, sc)
        break
    if count == 1:
        #print(mv_count, shark, sr, sc)
        r, c = fish[0][0], fish[0][1]
        dist = get_distance(r, c)
        if dist >= 0:   # Eatable
            mv_count += dist
            counter += 1
            set_shark()
            plain[sr][sc] = 0   # Away
            sr, sc = r, c
            plain[sr][sc] = 9   # EAT
        else:
            break

    if count >= 2:
        #print(mv_count, shark, sr, sc)
        min_d = 999

        for i in range(len(fish)):
            dist = get_distance(fish[i][0], fish[i][1])
            if 0 < dist < min_d:    # 더 가까우면
                min_d = dist
                select = i

        if min_d != 999:
            mv_count += min_d
            counter += 1
            set_shark()
            plain[sr][sc] = 0  # Away
            sr, sc = fish[select][0], fish[select][1]
            plain[sr][sc] = 9  # EAT
        else:
            break

print(mv_count)