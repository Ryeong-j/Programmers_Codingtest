def solution(board):
    n = len(board)
    m = len(board[0])

    mark = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m:
                            mark.add((ni, nj))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if (i,j) not in mark:
                cnt += 1
    return cnt


# def solution(board):
#     a = 0
#     b = []
    
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 1:
#                 b.append([i, j])
                
#     for i, j in b:
#         if i == 0 and j == 0:
#             board[i][j+1] = 1
#             board[i-1][j+1] = 1
#             board[i-1][j] = 1
#         elif i == 0 and j ==len(board)-1:
#             board[i-1][j-1] = 1
#             board[i-1][j] = 1
#             board[i][j-1] = 1
#         elif i == len(board)-1 and j == 0:
#             board[i][j+1] = 1
#             board[i-1][j] = 1
#             board[i-1][j+1] = 1
#         elif i == len(board)-1 and j == len(board)-1:
#             board[i-1][j-1] = 1
#             board[i-1][j] = 1
#             board[i][j-1] = 1
#         elif i == 0:
#             board[i][j-1] = 1
#             board[i][j+1] = 1
#             board[i+1][j-1] = 1
#             board[i+1][j] = 1
#             board[i+1][j+1] = 1
#         elif j == 0:
#             board[i-1][j] = 1
#             board[i-1][j+1] = 1
#             board[i+1][j] = 1
#             board[i+1][j+1] = 1
#             board[i][j+1] = 1
#         elif i == len(board)-1:
#             board[i-1][j-1] = 1
#             board[i-1][j] = 1
#             board[i-1][j+1] = 1
#             board[i][j-1] = 1
#             board[i][j+1] = 1
#         elif j == len(board)-1:
#             board[i-1][j-1] = 1
#             board[i-1][j] = 1
#             board[i][j-1] = 1
#             board[i+1][j] = 1
#             board[i+1][j-1] = 1
#         else:
#             board[i-1][j-1] = 1
#             board[i-1][j] = 1
#             board[i-1][j+1] = 1
#             board[i][j-1] = 1
#             board[i][j+1] = 1
#             board[i+1][j-1] = 1
#             board[i+1][j] = 1
#             board[i+1][j+1] = 1
    
#     cc=0
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 0:
#                 cc+=1
#     return cc

# def solution(board):
#     answer = 0
#     a = []
#     b = []
#     c=0
    
#     for i in range()
    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         if board[i][j] == 1:
    #             board[i-1][j-1] = 1
                
                
                # a.append([i-1, j])
                # a.append([i-1, j+1])
                # a.append([i, j-1])
                # a.append([i, j])
                # a.append([i, j+1])
                # a.append([i+1, j-1])
                # a.append([i+1, j])
                # a.append([i+1, j+1])

    # b= list(set([tuple(set(item)) for item in a]))



#len(board)*len(board[0]) -len(b)
    # return b

#     22 23 24
#     32 33 34
#     42 43 44
    

# 00000
# 00000
# 00000
# 00110
# 00000

# 00000
# 00000
# 00010
# 00100
# 00000