from sys import exit

s = list(input())
t = list(input())

def dfs(s: list, t: list):
    print(s)
    if len(s) == len(t):
        if s == t:
            print(1)
            exit()
        else:
            return

    if s[0] == 'A':
        t.pop()
        dfs(s, t)
        s.pop()

    else:
        s.append('B')
        s.reverse()
        dfs(s, t)
        s.reverse()
        s.pop()

dfs(s, t)
print(0)