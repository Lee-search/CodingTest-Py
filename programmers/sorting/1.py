def solution(array, commands):
    answer = []

    for i, j, k in commands:
        t_array = array[i - 1:j]
        t_array.sort()
        answer.append(t_array[k - 1])
    return answer