def solution(arr):
    stk = []
    i=0
    
    while i < len(arr):
        if i < len(arr):
            if not stk:
                stk.append(arr[i])
                i+=1

            elif arr[i]==stk[-1]:
                stk.pop()
                i+=1
            # elif arr[i]!=stk[-1]:
            else:
                stk.append(arr[i])
                i+=1

    if not stk:
        return [-1]
        
    return stk