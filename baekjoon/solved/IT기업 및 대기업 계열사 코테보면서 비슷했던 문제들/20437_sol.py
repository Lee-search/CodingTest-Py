# https://www.acmicpc.net/problem/20437
# 문자열 게임: 슬라이딩 윈도우, defaultdict 사용 예제
# 인덱스 내 원소의 .count() 함수 접근 시 시간복잡도 O(N^2) 이므로 Counter 사용

from collections import defaultdict, Counter
import sys
input = sys.stdin.readline

def game(words, k):
    dic = defaultdict(list)
    max_answer = 0
    min_answer = len(words)

    # k개 이상인 것만 key: 단어, value: 위치 dict 저장
    c = Counter(words)
    for i in range(len(words)):
        # if words.count(words[i]) >= k:    # 시간초과 원인
        if c[words[i]] >= k:
            dic[words[i]].append(i)
    
    # 각각의 문자에 대해 k개씩 검증
    for x in dic.values():
        #print("dict: ", x)
        for j in range(len(x) - k + 1):
            tmp = x[j + k - 1] - x[j] + 1
            max_answer = max(tmp, max_answer)
            min_answer = min(tmp, min_answer)
    
    # 결과문 출력
    if max_answer == 0 and min_answer == len(words):
        print(-1)
        return
    print(min_answer, max_answer)

T = int(input())
for _ in range(T):
    words = list(input())
    k = int(input())
    game(words, k)