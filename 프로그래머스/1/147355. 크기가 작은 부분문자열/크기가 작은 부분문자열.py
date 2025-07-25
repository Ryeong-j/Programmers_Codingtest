def solution(t, p):
    answer = 0

    for i in range(len(t)-len(p)+1):
        n = t[i:len(p)+i]
        if int(n) <= int(p):
            answer+=1
    return answer