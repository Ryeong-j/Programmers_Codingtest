def solution(array, n):
    a=[]
    b=0
    array.sort()
    
    for i in array:
        a.append(abs(i-n))
        
    m=a.index(min(a))
        
    return array[m]


# def solution(array, n):
#     b=n
#     # m=0
    
#     for i in sorted(array):
#         if b>abs(i-n):
#             b=abs(i-n)
#             m=i
#             return i
