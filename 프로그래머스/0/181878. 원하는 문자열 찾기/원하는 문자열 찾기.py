def solution(myString, pat):
    answer = 0

    for i in range(len(myString)):
        if myString[i:i+len(pat)].upper()==pat.upper():
            return 1

    return 0