def solution(id_pw, db):
    answer = ''
    
    if id_pw[1] not in db:
        answer= 'fail'
    
    for i,j in db:
        if id_pw[0] == i and id_pw[1] == j:
            answer = 'login'
            break
        elif id_pw[0] == i:
            answer = 'wrong pw'
        # elif id_pw[1] == j:
        #     answer= 'fail'
      

    return answer