def solution(m):
    m=list(m.split(" "))
    a=0
    for i in range(len(m)):
        print(m[i])
        if i == 0:
            a+=int(m[i])
        elif m[i] == '+':
            a+=int(m[i+1])
            print(a)
        elif m[i] == '-':
            a-=int(m[i+1])
            print(a)

    return a
