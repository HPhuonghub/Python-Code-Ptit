for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = {}
    for j in a:
        if j in b:
            b[j] += 1
        else:
            b[j] = 1
    for j in b:
        if b[j] % 2 == 1:
            print(j)
            break
