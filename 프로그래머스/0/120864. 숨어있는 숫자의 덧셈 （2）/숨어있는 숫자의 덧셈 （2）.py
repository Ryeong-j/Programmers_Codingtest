def solution(m):
    answer = 0
    a=''
    
    for i in m:
        if 47 < ord(i) < 58:   #isdigit 사용하기
            a+=i
        else:
            if a != '':
                answer+=int(a)
                a=''
    if a != '':
        answer+=int(a)        
        
    return answer