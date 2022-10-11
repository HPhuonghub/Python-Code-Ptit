for i in range(int(input())):
    p,q = [x for x in input().split()]
    x1 = input().strip()
    if(x1.count(' ')) : x1, x2 = x1.split()
    else : x2 = input()
    mins = min(p, q)
    maxs = max(p, q)
    print(int(x1.replace(maxs, mins)) + int(x2.replace(maxs, mins)), end=" ")
    print(int(x1.replace(mins, maxs)) + int(x2.replace(mins, maxs)))