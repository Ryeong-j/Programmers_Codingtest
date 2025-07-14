def solution(my_string):
    answer = []

    for i in my_string:
        if 48<=ord(i) and ord(i)<=58:
            answer.append(int(i))
    answer.sort()
    
    return answer