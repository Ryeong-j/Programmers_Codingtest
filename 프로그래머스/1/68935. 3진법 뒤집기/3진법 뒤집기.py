def solution(n):
    answer = 0
    a=[]
    
    while n>0:
        a.append(n%3)
        n=n//3
        
    b=0
    a.reverse()

    for i in a:
        answer+= i* (3**b)
        b+=1
        
    return answer