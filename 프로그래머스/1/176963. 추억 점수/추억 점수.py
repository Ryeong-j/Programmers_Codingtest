def solution(name, yearning, photo):
    answer = []
    a=0
    for i in photo:
        for j in i:
            if j in name:
                print(yearning[name.index(j)])
                a += yearning[name.index(j)]

        answer.append(a)
        a = 0
        
    return answer


