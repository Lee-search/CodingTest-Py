from collections import deque

def solution(begin, target, words):
    # words 에 target 이 없으면 종료
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))

    while queue:
        now, count = queue.popleft()
        if now == target:
            return count

        # 각각의 words 에 대해
        # 틀린 단어의 수 계산 -> 1인 것만 append
        for w in words:
            differ = 0
            for i in range(len(now)):
                if now[i] != w[i]:
                    differ += 1

            if differ == 1:
                queue.append((w, count + 1))

    # 답을 찾지 못하고 queue가 비어버린 경우
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))