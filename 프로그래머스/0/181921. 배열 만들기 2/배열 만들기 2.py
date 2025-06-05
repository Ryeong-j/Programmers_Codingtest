def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        for ch in str(i):
            if ch != '0' and ch != '5':
                break
        else:
            answer.append(i)

    if not answer:
        return [-1]

    return answer