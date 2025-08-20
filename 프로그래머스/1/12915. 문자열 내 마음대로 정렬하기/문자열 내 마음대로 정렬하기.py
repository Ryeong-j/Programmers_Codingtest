# def solution(strings, n):
#     answer = []
#     a=[]
#     for i in strings:
#         answer.append(i[n])
#         answer.sort()
        
#     for i in range(1, len(strings)):
#         if answer.index(answer[strings[i]]) == answer.index(answer[strings[i-1]]):
#             answer[i] += 1
    
#     for i in strings:
#         print(answer.index(i[n]))
#         # a[answer.index(i[n])].append(i)

#     return a

def solution(strings, n):
    length = len(strings)
    
    # 버블 정렬로 직접 구현
    for i in range(length):
        for j in range(0, length - i - 1):
            # n번째 문자 우선 비교
            if strings[j][n] > strings[j+1][n]:
                strings[j], strings[j+1] = strings[j+1], strings[j]
            # n번째 문자가 같으면 전체 문자열 비교
            elif strings[j][n] == strings[j+1][n]:
                if strings[j] > strings[j+1]:
                    strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings