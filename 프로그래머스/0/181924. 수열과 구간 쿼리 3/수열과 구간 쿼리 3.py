def solution(arr, queries):
    
    for query in queries:
        i=query[0]
        j=query[1]
    
        a=arr[i]
        arr[i]=arr[j]
        arr[j]=a
        
    return arr