def solution(name):
    _name = [ord(each) for each in name]

    answer = 0
    for _ch in _name:
        if _ch <= ord('M'):
            answer += _ch - ord('A')
        else:
            answer += 1
            answer += ord('Z') - _ch
    return answer

# 문자열의 길이에 따라 처음엔 'AAAA' 로만 이루어져있음
print(solution('JEROEN'))