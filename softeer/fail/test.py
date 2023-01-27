# https://softeer.ai/practice/info.do?idx=1&eid=1309
# 성적평가/난이도 3: 시간 복잡도 탈락

n = int(input())
total_score = [0] * n
for _ in range(3):
    score = list(map(int, input().split()))
    rank = [1] * n # 순위표
    for i in range(n):
        total_score[i] += score[i]
        for j in range(n):
            if score[j] > score[i]:
                rank[i] += 1
    print(' '.join(str(s) for s in rank))

total_rank = [1] * n
for i in range(n):
    for j in range(n):
        if total_score[j] > total_score[i]:
            total_rank[i] += 1
print(' '.join(str(s) for s in total_rank))