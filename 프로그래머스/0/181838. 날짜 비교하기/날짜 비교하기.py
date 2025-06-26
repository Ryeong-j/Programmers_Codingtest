def solution(date1, date2):
    a, b = '', ''
    
    for i in date1:
        a+=str(i)
    for i in date2:
        b+=str(i)
    if int(a)<int(b):
        return 1
    else:
        return 0
