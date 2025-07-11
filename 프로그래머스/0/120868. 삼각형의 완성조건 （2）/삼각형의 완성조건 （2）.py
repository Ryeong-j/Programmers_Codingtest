# def solution(sides):
#     answer = 0
    
#     for i in range(1001):
#         if i < sum(sides) and i >= max(sides):
#             answer+=1
#         elif i==sides[0] and i == sides[1]:
#             answer+=1
    
#     m=max(sides)
#     sides.remove(m)

#     for i in range(m):
#         if i+sides[0] > m:
#             answer+=1
            
#     return answer

def solution(sides):
    a, b = sides
    min_x = abs(a - b) + 1
    max_x = a + b - 1
    
    return max_x - min_x + 1
