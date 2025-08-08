def solution(a, b):
    answer = 0
    if a > b or a==b:
        max=a
        min=b
    elif a < b:
        max=b
        min=a
    
    for i in range(min, max+1):
        answer+=i
    return answer