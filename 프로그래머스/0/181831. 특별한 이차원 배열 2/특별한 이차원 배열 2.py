def solution(arr):
    answer = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer = 1
            else: 
                return 0
    return answer