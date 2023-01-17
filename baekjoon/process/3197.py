import copy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

plain = []
ducks = []
ice_queue = deque()   # 얼음만 추려서 위치 저장
# 물은 0, 얼음은 1로 저장
for r in range(n):
    line = []
    for c, ch in enumerate(input()):
        # 오리는 따로 추려서 ducks 배열에 저장
        if ch == 'L':
            ducks.append((r, c))
        if ch == 'X':
            line.append(1)
            ice_queue.append((r, c))
        else:
            line.append(0)
    plain.append(line)

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(start, end, visited):
    start_r, start_c = start
    end_r, end_c = end

    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True

    while q:
        now_r, now_c = q.popleft()
        # 두 오리가 서로 만나면 True 리턴
        if now_r == end_r and now_c == end_c:
            return True
        
        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]

            if 0 <= next_r < n and 0 <= next_c < m:
                if not visited[next_r][next_c]:
                    if plain[next_r][next_c] == 0:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True
    return False

# 하루가 지난 뒤의 plain 상태 제작
def melt_snow():
    _plain = copy.deepcopy(plain)
    for _ in range(len(ice_queue)):
        i, j = ice_queue.popleft()

        # 현재 블럭이 얼음 -> 녹을 수 있나 확인
        for d in range(4):
            near_i = i + dr[d]
            near_j = j + dc[d]

            # 존재하지 않는 구역
            if 0 > near_i or near_i >= n or 0 > near_j or near_j >= m:
                ice_queue.append((i, j))
                continue

            # 옆이 얼음이라 녹지 않는 경우
            if _plain[near_i][near_j] == 1:
                ice_queue.append((i, j))
                continue

            plain[i][j] = 0
            break

start_duck = ducks[0]
end_duck = ducks[1]
answer = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]

    if bfs(start_duck, end_duck, visited):
        print(answer)
        break

    melt_snow()
    answer += 1