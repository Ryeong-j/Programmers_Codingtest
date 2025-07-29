def solution(dots):
    # 1. (0,1)-(2,3)
    dx1, dy1 = dots[0][0]-dots[1][0], dots[0][1]-dots[1][1]
    dx2, dy2 = dots[2][0]-dots[3][0], dots[2][1]-dots[3][1]
    if dx1 * dy2 == dx2 * dy1:
        return 1
    
    # 2. (0,2)-(1,3)
    dx1, dy1 = dots[0][0]-dots[2][0], dots[0][1]-dots[2][1]
    dx2, dy2 = dots[1][0]-dots[3][0], dots[1][1]-dots[3][1]
    if dx1 * dy2 == dx2 * dy1:
        return 1

    # 3. (0,3)-(1,2)
    dx1, dy1 = dots[0][0]-dots[3][0], dots[0][1]-dots[3][1]
    dx2, dy2 = dots[1][0]-dots[2][0], dots[1][1]-dots[2][1]
    if dx1 * dy2 == dx2 * dy1:
        return 1

    return 0
