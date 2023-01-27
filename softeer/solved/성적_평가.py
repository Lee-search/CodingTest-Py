# https://softeer.ai/practice/info.do?idx=1&eid=1309
# 성적평가/난이도 3: 정렬, 튜플 자료구조 심화편

import sys
input = sys.stdin.readline

n = int(input())

# 개인 성적
total_score = [0] * n
for _ in range(3):
    score = list(map(int, input().split()))
    ranking = [1] * n
    for i in range(n):
        total_score[i] += score[i]
        score[i] = (score[i], i)
    score.sort(key=lambda x: x[0])

    for i in range(n):
        ranking[score[i][1]] = n - i
        # 직전 사람의 점수와 현재 사람의 점수가 같은 경우
        if i >= 1 and score[i][0] == score[i - 1][0]:
            # 같은 등수로 변경하고 건너뛰기
            for j in range(i - 1, -1, -1):
                if i >= 1 and score[i][0] == score[j][0]:
                    ranking[score[j][1]] = ranking[score[i][1]]
                else:
                    break

    print(' '.join(str(s) for s in ranking))

# 종합 성적
total_ranking = [1] * n
for i in range(n):
    total_score[i] = (total_score[i], i)
total_score.sort(key=lambda x: x[0])

for i in range(n):
    total_ranking[total_score[i][1]] = n - i
    # 순위가 연속해서 바뀌는 경우 고려
    for j in range(i - 1, -1, -1):
        if i >= 1 and total_score[i][0] == total_score[j][0]:
            total_ranking[total_score[j][1]] = total_ranking[total_score[i][1]]
        else:
            break

print(' '.join(str(s) for s in total_ranking))