def solution(arr, inter):
    answer = []
    
    for i in inter:
        answer+=arr[i[0]:i[1]+1]
            
    return answer