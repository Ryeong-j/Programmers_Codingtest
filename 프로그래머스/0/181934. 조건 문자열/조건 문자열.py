def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq=='>':
        if eq=="=" and n>=m:
            answer= 1
        elif eq=='=' and n>=m:
            answer= 0
        elif eq=="!" and n>m:
            answer= 1
        else:
            answer= 0
            
    if ineq=='<':
        if eq=="=" and n<=m:
            answer= 1
        elif eq=='=' and n<=m:
            answer= 0
        elif eq=="!" and n<m:
            answer= 1
        else:
            answer= 0
            
    return answer