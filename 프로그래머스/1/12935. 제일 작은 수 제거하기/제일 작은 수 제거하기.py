def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    
    if len(arr) == 0:
        return [-1]
    else:
        return arr