from collections import deque

def solution(tickets):

    def next_ticket(port):
        for start, end in sorted(tickets):
            if start == port:
                return [start, end]

    queue = deque()
    queue.append(next_ticket("ICN"))

    print("ICN", end=" ")

    while queue:
        s_port, e_port = queue.popleft()
        print(e_port, end=" ")
        queue.append(next_ticket(e_port))

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# --> ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# --> ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]