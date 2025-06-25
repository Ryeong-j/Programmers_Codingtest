def solution(arr, d):
    a = []
    for i in arr:
        if i not in d:
            a.append(i)
    return a
