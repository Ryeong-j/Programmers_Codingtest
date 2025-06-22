def solution(arr):
    first = -1
    last = -1
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            if first == -1:
                first = i
            last = i

    if first == -1:
        return [-1]

    for j in range(first, last + 1):
        answer.append(arr[j])

    return answer

