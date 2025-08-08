def solution(s):
    pp=0
    yy=0
    
    for i in s:
        if i == 'p' or i=='P':
            pp+=1
        elif i=='y' or i=='Y':
            yy+=1
      
    if pp==yy:
        return True
    else:
        return False