def solution(arr, queries):
    
#     for query in queries:
#         for i in range(query[0],query[1]+1):
#             arr[i]+=1
        
#     return arr

    for i, j in queries:
        for n in range(i, j+1):
            arr[n]+=1
    
    return arr