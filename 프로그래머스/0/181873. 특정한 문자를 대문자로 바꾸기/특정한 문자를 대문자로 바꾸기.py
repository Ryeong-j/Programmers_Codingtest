def solution(mg, alp):
    answer = ''
    
    for i in mg:
        if i == alp:
            answer+=i.upper()
        else:
            answer+=i
    return answer