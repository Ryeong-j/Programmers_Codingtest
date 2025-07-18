def solution(before, after):
#     a= list(after)
    
#     for i in before:
#         if i in a:
#             a.remove(i)
            
#     if not a:
#         return 1
#     else:
#         return 0
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0