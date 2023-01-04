# 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
def solution(maps):
    m = len(maps)  # x
    n = len(maps[0])  # y

    #visited = [[False] * n] * m
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = 10000
    def dfs(x, y, steps):
        if x == m - 1 and y == n - 1:
            nonlocal answer
            answer = min(answer, steps)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 좌표값이 외부로 나가는 경우
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 좌표값이 벽으로 막혀있는 경우
            if not maps[nx][ny]:
                continue

            #print("called: ", nx, ny)
            maps[nx][ny] = 0
            dfs(nx, ny, steps + 1)
            maps[nx][ny] = 1

    dfs(x=0, y=0, steps=1)
    return answer if answer != 10000 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # --> 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # --> -1