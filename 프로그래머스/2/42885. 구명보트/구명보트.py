def solution(people, limit):
    a=0
    start=0
    end=len(people)-1
    people.sort()
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start+=1
        end-=1
        a+=1
            
    return a