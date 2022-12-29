def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    for i in _reserve:
        next, last = i + 1, i - 1
        
        # 앞에 있는 것 먼저 검증
        if last in _lost:
            _lost.remove(last)
        elif next in _lost:
            _lost.remove(next)

    return n - len(_lost)