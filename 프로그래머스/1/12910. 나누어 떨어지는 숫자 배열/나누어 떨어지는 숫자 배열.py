def solution(arr, divisor):
    # divisor로 나누어 떨어지는 값만 필터링
    answer = [x for x in arr if x % divisor == 0]

    # 나누어 떨어지는 값이 없으면 [-1] 반환
    if not answer:
        return [-1]

    # 오름차순 정렬 후 반환
    return sorted(answer)
