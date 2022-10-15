def nt(n):
    if n < 2:
        return 0
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return 0
        return 1


m = {}
n = int(input())
a = [int(x) for x in input().split()]
for i in a:
    if nt(i) == 1:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
for i in m:
    print(i, m[i])
