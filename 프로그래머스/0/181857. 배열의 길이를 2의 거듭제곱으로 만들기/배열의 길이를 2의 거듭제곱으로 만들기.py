# import math
# def solution(arr):
#     answer = []
    
#     if math.sqrt(len(arr)) != 2:
#         for j in range(len(arr)):
#             a=2**j-len(arr)
#             b=min(a)
#             for i in range(2**b-len(arr)):
#                 arr.append(0)
#                 if math.sqrt(len(arr)) ==2:
#                     break
            
#     return arr

import math

def solution(arr):
    n = 1

    while n < len(arr):
        n *= 2

    arr += [0] * (n - len(arr))

    return arr