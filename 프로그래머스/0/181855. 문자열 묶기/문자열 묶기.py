# def solution(strArr):
#     count=[]
    
#     for i in strArr:
#         if len
#     return max(a,b,c)

def solution(strArr):
    counter = {}
    for s in strArr:
        l = len(s)
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1
    if not counter:  # 빈 리스트 처리
        return 0
    return max(counter.values())