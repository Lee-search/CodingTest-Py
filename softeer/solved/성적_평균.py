# https://softeer.ai/practice/info.do?idx=1&eid=389
# 성적 평균/난이도 3: 반올림 및 f-string 활용
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))
for _ in range(k):
    a, b = map(int, input().split())
    # a, b 사이 구간의 평균 반올림해서 출력
    # f-string 을 통해 소숫점 자리수 출력
    # ex) f'{0.33333}:.2f' -> 0.33
    print(f'{round(sum(S[a - 1:b]) / (b - a + 1), 2):.2f}')