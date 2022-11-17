def compare(s_i: int, w_i: int) -> int:
    if w_i == len(w) or s_i == len(stream):
        return -1
    if w_i == len(w) - 1 and stream[s_i] == w[w_i]:
        return 1
    if stream[s_i] == w[w_i]:
        return compare(s_i + 1, w_i + 1)
    return -1

for n in range(1, 11):
    N = int(input())
    w = input()
    stream = input()
    cnt = 0

    for i in range(len(stream)):
        if compare(i, 0) == 1:
            cnt += 1
            i += len(w) - 1

    print(f'#{n} {cnt}')