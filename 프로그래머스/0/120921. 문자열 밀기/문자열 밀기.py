def solution(A, B):
    n = len(A)
    for i in range(n):
        # 한 번 밀 때마다 문자열을 '오른쪽으로' 한 칸씩 shift
        shifted = A[-i:] + A[:-i] if i != 0 else A
        if shifted == B:
            return i
    return -1
