def solution(chicken):
#     answer = 0
#     a = []
    
#     while chicken:
#         a.append(chicken % 10)
#         chicken = chicken // 10
#         answer+=chicken
        
#     if sum(a)>=10:
#         answer+=sum(a)//10
#         if sum(a)%10+sum(a)//10 >= 10:
#             answer+=(sum(a)%10+sum(a)//10)//10
 
#     return answer

# 10951
# 1095    1
#  109     5
#   10      9
#    1      1
#   1215

    answer = 0
    a = 0
    
    while chicken:
        a+=chicken % 10
        chicken = chicken // 10
        answer+=chicken
        
    if a>=10:
        answer+= a//10
        if a%10+a//10 >= 10:
            answer+=(a%10+a//10)//10
 
    return answer