def solution(m, pat):
    a=''
    for i in m:
        if i == 'A':
            a+='B'
        else: 
            a+='A'


    if pat in a:
        return 1
    else: 
        return 0