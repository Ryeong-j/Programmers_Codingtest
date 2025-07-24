def solution(n):
    cnt = 0
    num = 0
    while cnt < n:
        num += 1
        # 3의 배수이거나 3이 포함된 수는 패스
        if num % 3 == 0 or '3' in str(num):
            continue
        cnt += 1
    return num

