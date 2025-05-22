def solution(arr, queries):
    answer = []
    add = []    
    
    for query in queries:
        for i in range(query[0], query[1]+1):
            
            if arr[i] > query[2]:
                add.append(arr[i])
                
        if add != []:
            answer.append(min(add))
            add = []

        else:
            answer.append(-1)
            
    return answer