def solution(emergency):
    answer = []
    a = {}
    
    for i in sorted(emergency):
        a[i]= len(emergency)-emergency.index(i)
        answer.append(a[i])

    return answer

#sorted(emergency, reverse=True)를 사용하면 복잡한 조건 쓸 필요없음