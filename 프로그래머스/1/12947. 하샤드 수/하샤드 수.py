def solution(x):
    
    s=str(x)
    a=0
    
    for i in s:
        a+=int(i)
    print(a)
    if x % a == 0:
        return True
    else:
        return False
