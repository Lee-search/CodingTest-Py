# 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 미완성 소스코드 - 정답 1, 2 통과 안됨

def solution(tickets):
    # 원래 티겟의 갯수
    n_ticket = len(tickets)

    # IN: 출발공항 -> OUT: 사용할 티켓
    def next_ticket(port):
        next = []
        for s_port, e_port in tickets:
            if port == s_port:
                next.append([s_port, e_port])
        if len(next) == 0:
            return
        # 알파벳 순서가 앞에 오는 항공권 리턴
        elif len(next) >= 2:
            return sorted(next)[0]
        return next[0]

    def dfs(foot_print, port, count):
        # print(foot_print, port, count)
        if count == n_ticket:
            return

        info = next_ticket(port)
        if not info:
            return
        now_port, next_port = info

        tickets.remove([now_port, next_port])
        foot_print.append(next_port)
        dfs(foot_print, next_port, count + 1)
        # foot_print.remove(next_port)
        tickets.append([now_port, next_port])

    # 다녀간 공항 목록
    foots = ["ICN"]
    dfs(foots, "ICN", 0)

    return foots

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# --> ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# --> ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))
# --> ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]