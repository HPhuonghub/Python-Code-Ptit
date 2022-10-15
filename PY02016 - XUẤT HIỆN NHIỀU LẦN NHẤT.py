for i in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = [0] * 100000
    for i in a:
        b[i] += 1
    count = 0
    res = 0
    for i in range(len(b)):
        if b[i] > count:
            count = b[i]
            res = i
    if count > n//2:
        print(res)
    else:
        print("NO")
