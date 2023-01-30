h, w = map(int, input().split())
heights = list(map(int, input().split()))
blocks = [[0] * w for _ in range(h)]

# blocks: 블록 있으면 1 없으면 0
for c in range(w):
    for r in range(h - 1, h - 1 - heights[c], -1):
        blocks[r][c] += 1
print(blocks)

answer = 0
for r in range(h):
    # 플래그 T이면 공간의 숫자 세기 시작
    wall_on = False
    tmp = 0
    for c in range(w):
        if blocks[r][c] == 0:
            # 직전 칸이 벽이면 플래그 T
            if blocks[r][c - 1] == 1:
                wall_on = True
            tmp += 1
        
        elif blocks[r][c] == 1:
            # 직전 칸이 빈 공간이면 물 채우기
            if blocks[r][c - 1] == 0 and wall_on:
                wall_on = False
                answer += tmp
                tmp = 0

        print(r, c, tmp)
    print("answer: ", answer)

print(answer)

        

print(answer)