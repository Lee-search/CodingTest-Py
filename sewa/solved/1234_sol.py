def search(pwd: str, p_len: int) -> str:
    for i in range(1, p_len):
        if pwd[i - 1] == pwd[i]:
            pwd = pwd[:i - 1] + pwd[i + 1:]
            break

    if p_len == len(pwd):
        return pwd
    return search(pwd, len(pwd))

for test in range(1, 11):
    p_len, password = input().split()
    print('#' + str(test) + ' ' + search(password, int(p_len)))

