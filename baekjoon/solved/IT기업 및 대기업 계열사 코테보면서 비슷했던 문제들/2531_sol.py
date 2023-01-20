# https://www.acmicpc.net/problem/2531
# 회전 초밥: 투 포인터와 다익스트라 배열 이용

# 접시 수, 종류, 연속해서 먹는 접시 수, 쿠폰번호
n, d, k, c = map(int, input().split())
chain = [int(input()) for _ in range(n)]
chain.extend(chain) # 끝자락 itor 에서 리스트 아웃 방지

answer = 0
for i in range(n):
    eaten_array = [0] * (d + 1)
    left, right = i, i + k
    
    # 먹은 스시의 수
    total = 0

    # 연속된 k개의 스시 비교
    for s in chain[left:right]:
        if eaten_array[s] == 0:
            eaten_array[s] += 1
            total += 1
    # 쿠폰 비교
    if eaten_array[c] == 0:
        #eaten_array[c] += 1
        total += 1
            
    answer = max(answer, total)

print(answer)