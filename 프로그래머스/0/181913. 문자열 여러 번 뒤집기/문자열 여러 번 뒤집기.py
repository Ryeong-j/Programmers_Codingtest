def solution(ms, queries):
    
    for s,e in queries:
        ms= ms[:s]+ms[s:e+1][::-1]+ms[e+1:]
               
    return ms