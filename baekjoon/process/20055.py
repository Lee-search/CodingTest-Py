n, k = map(int, input().split())
armor_array = list(map(int, input().split()))    # 내구도 어레이
visited = [False] * (2 * n)                 # 로봇 방문 여부

cnt = 0
steps = 1
while cnt < k:
    visited[0] = True
    # 옆 자리 내구도 1 이상이며 이미 올라탄 로봇 없으면 이동 가능
    if armor_array[1] != 0 and not visited:
        visited[1] = True
        visited[0] = False
        armor_array[1] -= 1

    if

def move_robit(pos):
    # 내구도 1 이상이며 이미 올라탄 로봇 없으면 이동 가능
    if armor_array[pos] != 0 and not visited:
        visited[pos] = True
        visited[pos - 1] = False
        armor_array[pos] -= 1
        move_robit(pos + 1)
