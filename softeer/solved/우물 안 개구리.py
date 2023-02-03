# https://softeer.ai/practice/info.do?idx=1&eid=394
# 우물 안 개구리: DP

n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.insert(0, 0)

# 친분이 있는 인물 간 연결 테이블 작성
related = [[] for _ in range(n + 1)]
for _ in range(m):
    p_1, p_2 = map(int, input().split())
    related[p_1].append(p_2)
    related[p_2].append(p_1)

# -1: 패배, 0: 중립, 1: 승리
winner = [0] * (n + 1)
# 각 인물의 생각 조사
for i in range(1, n + 1):
    # 친분이 없는 경우
    if len(related[i]) == 0:
        winner[i] = 1
        continue

    # 앞선 경우에서 패배한 경우
    if winner[i] == -1:
        continue

    for j in related[i]:
        # 내가 이긴 사람 카운트
        if weights[i] > weights[j]:
            winner[i] = 1
            winner[j] = -1
        elif weights[i] == weights[j]:
            winner[i] = -1
            winner[i] = -1
            break
        else:
            winner[i] = -1
            break

print(winner.count(1))