def solution(emergency):
    answer = []
    a = {}
    
    for i in sorted(emergency):
        a[i]= len(emergency)-emergency.index(i)
        answer.append(a[i])

    return answer