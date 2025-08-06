def solution(board):
    n = len(board)
    danger = [[0]*n for _ in range(n)]
    
    # 8방향 좌표 (상, 하, 좌, 우, 대각선)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger[i][j] = 1 # 지뢰가 있는 칸
                # 주변 8방향을 danger로 설정
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = 1
                        
    # 안전한 지역(0) 세기 
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_count += 1
    return safe_count


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