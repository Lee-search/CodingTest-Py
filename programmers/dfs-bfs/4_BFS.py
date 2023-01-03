from collections import deque

def solution(begin, target, words):
    # 추가, words 에 target 이 없으면 종료
    if target not in words:
        return 0

    visited = [False] * len(words)

    queue = deque()
    queue.append((begin, 0))

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        for i in range(len(current)):
            front = current[:i]
            back =  current[i + 1:]

            for j, w in enumerate(words):
                w_front = w[:i]
                w_back = w[i + 1:]

                if front == w_front and back == w_back:
                    if w != current and not visited[j]:
                        queue.append((w, count + 1))
                        visited[j] = True

    # 답을 찾지 못하고 queue가 비어버린 경우
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))