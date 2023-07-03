for _ in range(int(input())):
    score_array = [0] * 101  # 0 ~ 100점

    t = int(input())
    stu_array = list(map(int, input().split()))

    for i in range(1000):
        score_array[stu_array[i]] += 1

    current = 0  # 가장 큰 값
    answer = 0 # 가장 큰 점수

    for j in range(100):
        # 가장 큰 점수 출력을 위해 같아도 변경
        if score_array[j] >= current:
            answer = j
            current = score_array[j]

    print(f'#{t} {answer}')