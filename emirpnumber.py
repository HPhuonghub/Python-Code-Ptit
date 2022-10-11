def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        return 1
for i in range(int(input())):
    n = int(input())
    a = []
    for i in range(13,n+1):
        m = int(str(i)[::-1])
        if nt(i) and nt(m) and i!=int(m) and m<=n:
            h = 0
            for j in a:
                if i == j: h=1
            if h!=1:
                a.append(i)
                a.append(m)
    for i in a:
        print(i,end=" ")
    print()