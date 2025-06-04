def solution(numlog):
    answer=''
    
    for i in range(len(numlog)-1):
        a= numlog[i+1] - numlog[i]
        
        if a==1:
            answer+='w'
        elif a==-1:
            answer+='s'
        elif a==10:
            answer+='d'
        else:
            answer+='a'
            
    return answer