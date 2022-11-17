for i in range(1, 11):
    N = int(input())
    builds = list(map(int, input().split()))
    answer = sum([min(builds[i] - max(builds[i - 1], builds[i - 2]), builds[i] - max(builds[i + 1], builds[i + 2])) for i in range(2, N - 1) if builds[i - 1] < builds[i] and builds[i - 2] <= builds[i] and builds[i] > builds[i + 1] and builds[i] > builds[i + 2]])
    print(f"#{i} {answer}")
