def solution(n):
    # 제곱근을 구해서 정수 부분만 남긴 뒤, 제곱했을 때 n과 같으면 제곱수입니다.
    return 1 if int(n**0.5)**2 == n else 2

