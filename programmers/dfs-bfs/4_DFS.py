# 단어변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    visited = [False] * len(words)

    # 타겟을 만들 수 없는 경우
    if target not in words:
        return 0

    # 깊이 체크, 1 -> T / 2~ -> F
    def check_differ(w, tmp_w):
        differ = 0
        for j in range(len(w)):
            if tmp_w[j] != w[j]:
                differ += 1

        if differ == 1:
            return True
        return False
    
    # 입력 조건 -> 최대 50개의 단어
    answer = 50
    def dfs(word, count):
        nonlocal answer
        if count > answer:
            return

        if word == target:
            answer = min(answer, count)
            return
        
        # 각각의 단어에 대해 1개만 다른 단어 추출
        for i in range(len(words)):
            w_tmp = words[i]

            if not visited[i] and check_differ(word, w_tmp):
                visited[i] = True
                dfs(w_tmp, count + 1)
                visited[i] = False

        return

    dfs(begin, 0)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))