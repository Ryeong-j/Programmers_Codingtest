def solution(absolutes, signs):
    total = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            total += num
        else:
            total -= num
    return total
