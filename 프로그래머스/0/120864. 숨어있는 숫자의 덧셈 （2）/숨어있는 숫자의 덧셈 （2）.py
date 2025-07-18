# def solution(m):
#     answer = 0
#     a=''
    
#     for i in range(len(m)):
#         if 48 < ord(m[i]) < 58:
#             a+=m[i]
#         else:
#             if a != '':
#                 answer+=int(a)
#                 a=''
#     if a != '':
#         answer+=int(a)        
        
#     return answer

def solution(my_string):
    total = 0
    num = ""
    for ch in my_string:
        if ch.isdigit():        # 숫자인 경우
            num += ch           # 숫자를 이어 붙임
        else:                   # 문자인 경우
            if num != "":
                total += int(num)
                num = ""        # 숫자 저장 값 초기화
    if num != "":               # 마지막에 숫자로 끝나는 경우
        total += int(num)
    return total