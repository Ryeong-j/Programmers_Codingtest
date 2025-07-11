def solution(sides):
    answer = 0
    
    m=max(sides)
    n=sides.remove(m)
    
    if sum(sides)<=m:
        return 2
    else:
        return 1
