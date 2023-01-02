answer = 0  # --> 2
def solution(numbers, target):
    # numbers = [4, 1, 2, 1]
    # target = 4

    def dfs(position, total):
        if position == len(numbers):
            if total == target:
                global answer
                answer += 1
            return
        else:
            dfs(position + 1, total + numbers[position])
            dfs(position + 1, total - numbers[position])

    dfs(0, 0)
    global answer
    return answer

solution([4, 1, 2, 1], 4)
print(answer)