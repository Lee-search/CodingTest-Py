def solution(begin, target, words):
    visited = [False] * len(words)

    def dfs(w, count):
        if w == target:
            return count

        for i in range(len(words)):
            w_tmp = words[i]

            if not visited[i]:
                differ = 0
                for j in range(len(w)):
                    if w_tmp[j] != w[j]:
                        differ += 1

                if differ == 1:
                    print(w, w_tmp, count)
                    visited[i] = True
                    dfs(w_tmp, count + 1)

    return dfs(begin, 0) if dfs(begin, 0) != 0 else 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))