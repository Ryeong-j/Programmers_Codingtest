def solution(myString):
    answer = ''
    for i in myString:
        if i.lower() == 'a':
            answer += 'A'
        elif i.isupper():
            answer += i.lower()
        else:
            answer += i
    return answer