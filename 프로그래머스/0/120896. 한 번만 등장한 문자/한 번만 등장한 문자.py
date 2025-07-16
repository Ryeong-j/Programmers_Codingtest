def solution(s):
    ss=set(s)
    ls=list(s)
    
    for i in ss:
        if i in s:
            ls.remove(i)
    
    ss=[] 

    for i in s:
        if i not in ls:
            ss.append(i)
      
    return "".join(sorted(ss))

