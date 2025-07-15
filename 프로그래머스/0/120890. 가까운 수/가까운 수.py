def solution(array, n):
    a=[]
    array.sort()
    
    for i in array:
        a.append(abs(i-n))
        
    m=a.index(min(a))
        
    return array[m]


