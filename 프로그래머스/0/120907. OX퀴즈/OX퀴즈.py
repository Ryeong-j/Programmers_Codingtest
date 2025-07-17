def solution(quiz):
    answer = []

    for i in quiz:
        a=i.split('=')

        if eval(a[0])==int(a[1]):
            answer.append('O')
        else:
            answer.append('X')

    return answer

#eval안쓰는 버전
# def solution(quiz):
#     answer = []

#     for i in quiz:
#         a, op, b, eq, c = i.split() 
#         a= int(a)
#         b= int(b)
#         c= int(c)


#         if op == '+':
#             if a + b == c:
#                 answer.append('O')
#             else:
#                 answer.append('X')
#         else:
#             if a - b == c:
#                 answer.append('O')
#             else:
#                 answer.append('X')    

#     return answer