def solution(num_list):
    a, b = 0, 0

    for i in num_list[::2]:
        a += i
    for i in num_list[1::2]:
        b += i
        
    return max(a,b)

