def solution(my_string):
    answer = ''
    
    for j in my_string:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            continue
        else:
            answer+=j
    return answer