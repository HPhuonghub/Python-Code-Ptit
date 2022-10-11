for i in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    ok = 0
    for i in range(n):
        if a[i] > b[i]:
            ok = 1
            break
    if ok==0: print("YES")
    else: print("NO")