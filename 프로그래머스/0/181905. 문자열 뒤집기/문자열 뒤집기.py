# def solution(my_string, s, e):
#     answer = ''
    
#     for i in range(e-len(my_string),s-len(my_string)-1,-1):
#         answer=my_string[:s]+my_string[i]+my_string[e+1:]
    
#     return answer

def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]