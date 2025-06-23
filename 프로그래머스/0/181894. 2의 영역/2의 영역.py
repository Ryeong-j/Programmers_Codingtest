def solution(arr):
    answer = []
    a=[]
    
    for i in range(len(arr)):
        if arr[i]==2:
            answer.append(i)
    
    if not answer:
            return [-1]
    else:
        for j in range(answer[0],answer[-1]+1):
            a.append(arr[j])
        
    return a