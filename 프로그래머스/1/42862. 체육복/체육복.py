# def solution(n, lost, reserve):
    
#     for i in reserve:
#         if i in lost:
#             reserve.remove(i)
               
#     for i in reserve:
#         if i - 1 in lost:
#             lost.remove(i-1)
#         elif i + 1 in lost:
#             lost.remove(i+1)
            
#     return n - len(lost)

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    both = lost_set & reserve_set  # 여벌 있으면서 도난당한 학생
    
    lost_set -= both
    reserve_set -= both
    
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    
    return n - len(lost_set)
