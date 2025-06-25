def solution(m):
    answer = ''
    
    for i in m:
        if ord(i)<ord('l'):
            answer+='l'
        else:
            answer+=i
    return answer