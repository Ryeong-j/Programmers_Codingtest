# def solution(myString, pat):
#     answer = ''
#     for i in range(len(myString)):
#         answer = myString[:-i]
#         print(answer)
#         if answer[-len(pat):] == pat:
#             print(answer[-len(pat):])
#             break
            
#     return answer

def solution(myString, pat):
    
    a=myString.rfind(pat)
    return myString[:a+len(pat)]
        

