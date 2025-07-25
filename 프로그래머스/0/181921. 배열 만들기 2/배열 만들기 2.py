def solution(l, r):
    answer = []
    
#     for i in range(l, r+1):
#         if i % 5 == 0:
#             answer.append(i)

#     for i in answer:
#         a = i // 5
#         if '1' not in str(a) and '0' not in str(a):
#             print(a)
#         # if 1 not in a and 0 not in a:
#         #     answer.remove(i)
        
    for i in range(l, r+1):
        for j in str(i):
            if '5' != j and '0' != j:
                break
        else:
            answer.append(i)
    
    if not answer:
        return [-1]
    return answer