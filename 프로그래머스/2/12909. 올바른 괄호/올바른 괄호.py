def solution(s):
    answer = True
    a=0
    b=0
    c=list(s)
    
    if c[0]==')' or c[-1]=='(':
        return False
    
    for i in c:
        if i=='(':
            a+=1
        else:
            a-=1
        if a<0:
            return False
            
    if a==0:
        return True
    else:
        return False
    