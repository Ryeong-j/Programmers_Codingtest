def solution(s, ex):
    answer = ''
    
    for i in s:
        if ex not in i:
            answer+=i            
        
    return answer