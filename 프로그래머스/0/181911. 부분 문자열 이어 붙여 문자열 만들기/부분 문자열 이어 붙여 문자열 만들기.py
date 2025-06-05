def solution(my_strings, parts):
    answer = ''
    #print(my_strings[1][0:3])
    
    for i in range(len(parts)):
        s,e = parts[i]     
        answer += my_strings[i][s:e+1]
            
    return answer