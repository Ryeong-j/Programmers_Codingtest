def solution(numlist, n):
    answer = []
    a=[]
    b=[]
    numlist.sort(reverse=True)   
    
    for i in numlist:
        a.append(abs(n-i))
        
    for i in range(len(a)):
        m=min(a)
        b.append(numlist[a.index(m)])
        a[a.index(m)]+=max(numlist)

    return b