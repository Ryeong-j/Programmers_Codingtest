def solution(numbers):
    answer = ''
    a=''
    b={"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    
    for i in numbers:
        answer+=i
        if answer in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
            a+=str(b[answer])
            answer=''
            
    return int(a)

#replace써서 다시 풀어보기