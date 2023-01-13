# n x m 사이즈 지도
n, m = map(int, input().split())
# 시작좌표 (sr, sc) 시작방향 sd
sr, sc, sd = map(int, input().split())
plain = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m] * n

class Position():
    #now_row, now_col, now_direct = -1, -1, -1

    def __init__(self, start_row, start_col, start_direct):
        self.now_row = start_row
        self.now_col = start_col
        self.now_direct = start_direct

    def set_position(self, row, col, direct):
        self.now_row = row
        self.now_col = col
        self.now_direct = direct

    def get_position(self):
        return (self.now_row, self.now_col)

    def get_direct(self):
        return self.now_direct

def move(row: int, col: int, direct: int):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    nr = row + dr[direct]
    nc = col + dc[direct]

    if 0 < nr <= m and 0 < nc <= n:
        return (nr, nc)
    else:
        return (row, col)

def search(row: int, col: int, direct: int):
    if direct == 0:     new_d = 3
    elif direct == 1:   new_d = 0
    elif direct == 2:   new_d = 1
    else:               new_d = 2

    new_r, new_c = move(row, col, new_d)

def main():
    pos = Position(sr, sc, sd)
    while True:

        for i in range(4):
            flag = search(pos.now_row, pos.now_col, pos.now_direct + i)
            if flag:    # 이동할 수 있으면
                pos.set_position(pos.now_row, pos.now_col, pos.now_direct + i)
            else:
                pos.set_position()
