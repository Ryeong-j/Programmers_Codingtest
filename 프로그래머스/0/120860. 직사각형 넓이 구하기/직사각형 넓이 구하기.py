def solution(dots):
    x=[]
    y=[]
    
    for i, j in dots:
        x.append(i)
        y.append(j)
        
    return (max(x)-min(x)) * (max(y)-min(y))



