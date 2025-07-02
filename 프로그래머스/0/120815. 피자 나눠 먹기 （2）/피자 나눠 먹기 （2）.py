def solution(n):
    a=n
    b=6
    r=0
    
    while b!=0:
        r=a%b
        a=b
        b=r

    return n*6//a//6
    