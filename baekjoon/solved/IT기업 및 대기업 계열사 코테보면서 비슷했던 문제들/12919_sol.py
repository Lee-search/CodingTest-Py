# https://www.acmicpc.net/problem/12919
# A와B 2: 백트래킹 예제
# T -> S, 조건문 달아서 연산 숫자 감소
s = list(input())
t = list(input())

def dfs(t: list):
    if len(s) == len(t):
        if s == t:
            print(1)
            exit()
        else:
            return

    # 1.
    if t[-1] == 'A':
        t.pop()
        dfs(t)
        t.append('A')

    # 2.
    if t[0] == 'B':
        t.reverse()
        t.pop()
        dfs(t)
        t.append('B')
        t.reverse()

dfs(t)
print(0)