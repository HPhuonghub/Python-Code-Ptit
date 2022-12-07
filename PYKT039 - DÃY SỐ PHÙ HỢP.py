for i in range(int(input())):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    check = True
    for i in range(n):
        if a[i] > b[i]:
            check = False
    if check == True:
        print("YES")
    else:
        print("NO")
