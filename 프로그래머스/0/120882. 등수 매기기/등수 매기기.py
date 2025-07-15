def solution(score):
    answer = []
    a=[]
    for i, j in score:
        answer.append((i+j)/2)
        
    ans= sorted(answer, reverse=True)
    
    for i in answer:
        b = ans.index(i) + 1
        a.append(b)
            
    return a