chains = [''] # 톱니 4개, 0번은 사용 X
for _ in range(4):
    chains.append(input())
    
K = int(input()) # 회전 횟수
orders = []  # 회전 명령 (번호, 방향)
for _ in range(K):
    orders.append(list(map(int, input().split())))

def spin(chain: str, d: int) -> str:
    if d == -1:
        chain = chain[1:] + chain[0]
    else:
        chain = chain[7] + chain[:7]
    return chain

def check_left(main: str, left: str, d: int) -> str:
    if main[6] == left[2]:
        return left
    else:
        return spin(left, -d)

def check_right(main: str, right: str, d: int) -> str:
    if main[2] == right[6]:
        return right
    else:
        return spin(right, -d)

for o in orders:
    c = o[0] # 톱니 번호
    d = o[1] # 회전 방향
    lc, rc = c - 1, c + 1

    while lc > 0:
        span = check_left(chains[lc + 1], chains[lc], d)
        #print(f"{lc + 1} main: {chains[lc + 1]}, {lc} left: {chains[lc]} -> {s}")

        if span == chains[lc]:  # 같은 극이라 돌지 않았음
            break
        chains[lc] = span
        lc -= 1
        d *= -1

    d = o[1]
    while rc <= 4:
        span = check_right(chains[rc - 1], chains[rc], d)
        #print(f"{rc - 1} main: {chains[rc - 1]}, {rc} right: {chains[rc]} -> {s}")

        if span == chains[rc]:  # 같은 극이라 돌지 않았음
            break
        chains[rc] = span
        rc += 1
        d *= -1

    chains[c] = spin(chains[c], o[1])

print(sum(2 ** (i - 1) for i in range(1,5) if chains[i][0] == '1'), end='')