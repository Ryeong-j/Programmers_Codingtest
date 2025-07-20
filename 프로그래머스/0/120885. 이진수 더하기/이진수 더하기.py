# def solution(bin1, bin2):
#     answer = 0
#     aa=''
    
#     n1 = 0
#     n2 = 0
#     a = 1
#     for i in range(len(bin1)-1, -1, -1):
#         n1 += int(bin1[i]) * a
#         a *= 2

#     b = 1
#     for i in range(len(bin2)-1, -1, -1):
#         n2 += int(bin2[i]) * b
#         b *= 2
        
#     print(n1+n2)
#     while answer>0:
#         a+=str(answer % 2)
#         ansewr=answer//2
        
#     print(a)
#     return a

def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
