def solution(polynomial):

    answer = ''
    a=[]
    b=0
    for i in polynomial.split():
        if 'x' in i:
            if i[-2::-1] == '':
                a.append(1)
            else:
                a.append(int(i[0:len(i)-1]))
                print(a)
        elif i != '+' and i != ' ':
            b+=int(i)


    if len(a) != 0 and b!=0:
        if sum(a) != 1:
            answer=str(sum(a))+'x'+' + '+str(b)
        else: 
            answer='x'+' + '+str(b)
    elif len(a) == 0:
        answer=str(b)
    elif sum(a) == 1 and b == 0:
        answer='x'
    else:
        answer=str(sum(a))+'x'
    
    return answer
