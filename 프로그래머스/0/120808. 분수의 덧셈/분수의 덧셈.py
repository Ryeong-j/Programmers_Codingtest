def solution(numer1, denom1, numer2, denom2):
    answer = []
    ay=[]
    by=[]
    t=[]
    
    a = (numer1*denom2)+(numer2*denom1)
    b = denom1 * denom2
    
    m=min(a,b)
    
    for i in range(2,m+1):
        if a%i==0:
            ay.append(i)
        if b%i==0:
            by.append(i)
            
    for i in ay:
        for j in by:
            if i==j:
                t.append(i)
                
    if len(t)>0:
        answer.append(a/max(t))
        answer.append(b/max(t))
    else:
        answer.append(a)
        answer.append(b)
    
    return answer