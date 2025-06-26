def solution(keyinput, board):
    answer = [0,0]
    a=board[0]//2
    b=board[1]//2
    for i in keyinput:
        if i == 'up' and answer[1] < b:    
            answer[1] += 1
        elif i == 'down' and answer[1] > -b:
            answer[1] -= 1
        elif i == 'left' and answer[0] > -a:
            answer[0] -= 1
        elif i == 'right' and answer[0] < a:
            answer[0] += 1
            

    if answer[0]<0:
        answer[0]=max(answer[0],-a)
    else:
        answer[0]=min(answer[0],a)
            
    
    if answer[1]<0:
        answer[1]=max(answer[1],-b)
    else:
        answer[1]=min(answer[1],b)
                
    return answer



