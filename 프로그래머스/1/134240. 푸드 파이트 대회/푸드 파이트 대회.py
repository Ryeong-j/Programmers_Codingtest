# def solution(food):
#     answer = ''
#     n=0
#     f=food[1:]
#     for i in range(len(f)):
#         n=f[i]//2
#         if n>=1:
#             answer+=str(i+1)*n
#         else:
#             continue

#     return answer

def solution(food):
    answer = ''
    f = food[1:]

    for i in range(len(f)):
        n = f[i] // 2
        answer += str(i + 1) * n

    return answer + '0' + answer[::-1]

