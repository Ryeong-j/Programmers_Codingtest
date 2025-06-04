def solution(num_list):
    
    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else: 
        num_list.append(num_list[-1]*2)
        
    return num_list

#append()는 그 당시에 리스트만 수정할 뿐 값을 반환하진 않음 
#즉, answer=num_list.append(3)은 걍 null값임 