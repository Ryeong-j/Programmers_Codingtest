def solution(s):
    s=list(s)

    if s[0]=='-' and s[0]=='+':
        return s[0] + int(''.join(s[1:]))
    else:
        return int(''.join(s))
    
    print(''.join(s))