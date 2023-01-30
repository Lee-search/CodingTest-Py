# https://www.acmicpc.net/problem/1522
# 문자열 교환: 슬라이딩 윈도우 예씨
line = input()
# 'a'개수 세기
a_cnt = 0
for s in line:
    if s == 'a':
        a_cnt += 1

answer = 1000
n_line = len(line)
# 슬라이딩 윈도우를 위해 문자열 확장
line = line * 2
# 'a'개수 만큼의 구간에서 'b'의 개수가 가장 최소인 경우를 찾으면 됨
for i in range(n_line):
    b_cnt = 0
    for j in range(i, i + a_cnt):
        if line[j] == 'b':
            b_cnt += 1
    answer = min(answer, b_cnt)

print(answer)