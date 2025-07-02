def solution(array):
    a={}
    
    for i in array:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
            
    c = 0
    m=max(a.values())
    
    for i in a.values():
        if i == m:
            c+=1
        
    if c > 1:
        return -1
    else:
        for i in a:
            if a[i]==m:
                return i


    