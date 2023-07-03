t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    # 같은 경우는 차이가 0 -> 어짜피 반복문 시행 X
    differ = n - m
    if differ > 0:
        for _ in range(differ):
            m_list.append(0)
    else:
        for _ in range(-differ):
            n_list.append(0)

    answer = 0
    for _ in range(abs(differ) + 1):
        result = sum(n_list[i] * m_list[i] for i in range(len(n_list)))
        answer = max(answer, result)

        if n > m:
            m_list.insert(0, m_list.pop())
        else:
            n_list.insert(0, n_list.pop())

    print(f'#{test_case} {answer}')