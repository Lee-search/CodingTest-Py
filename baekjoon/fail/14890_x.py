import sys
input = sys.stdin.readline

N, L = map(int, input().split())
roads = []

for _ in range(N):  # Get N
    roads.append(list(map(int, input().split())))

for i in range(N):  # Get 2N
    temp = []
    for j in range(N):
        temp.append(roads[j][i])
    roads.append(temp)

## L 이 두개일때 기준으로만 구현하였음

##### MAIN #####
count = 0
for k in range(2 * N):
    # 모든 길에 대해서 검증 시작
    r = roads[k]
    l = [True] * N
    print("Start: ", r)
    for i in range(len(r)):
        if i == len(r) - 1: # 마지막 칸이면 -> 종료
            count += 1
            print("OK: ", r)
            break

        past, now, next = i - 1, i, i + 1
        # 다음 칸이 경사가 같으면,
        if r[now] == r[next]:
            past, now, next = i, i + 1, i + 2   # Move
            continue

        # 다음 칸이 경사가 다르면,
        # 1. 현재 칸보다 한칸 경사가 높고, 현재칸 + 이전 칸에 경사로를 깔 수 있는 경우
        if r[now] + 1 == r[next] and r[past] == r[now] and l[now] and l[past]:

            l[now], l[next] = False, False
            past, now, next = i, i + 1, i + 2  # Move

        # 2. 현재 칸보다 한칸 경사가 낮고, 앞으로 두칸 경사로를 깔 수 있는 경우
        elif r[now] - 1 == r[next] and next + 1 <= len(r) - 1 and r[next] == r[next + 1] and l[next] and l[next]:
            l[next], l[next + 1] = False, False
            past, now, next = i, i + 1, i + 2  # Move

        else:
            break   # 이동가능한 모든 케이스 조회

print(count)

