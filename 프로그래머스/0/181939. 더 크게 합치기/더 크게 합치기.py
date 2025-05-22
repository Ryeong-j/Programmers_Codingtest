def solution(a, b):
    a = str(a)
    b = str(b)
    answer1=a+b
    answer2=b+a
    
    if answer1>answer2 or answer1==answer2:
        return int(answer1)
    else:
        return int(answer2)
