def solution(n):
    answer = 0
    
    for i in range(1, n//10):
        if i**2 == n:
            return 1

    return 2
            
    # if answer % 2 == 0:
    #     return 2
    # else:
    #     return 1
