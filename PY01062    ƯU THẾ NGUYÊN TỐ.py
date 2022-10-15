def nt(n):
    if n < 2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0: return 0
        return 1
def solve(n):
    if nt(len(n)) != 1: return 0
    snt = 0
    nosnt = 0
    for i in range(0,len(n)):
        if nt(int(n[i]))==1: snt += 1
        else: nosnt += 1
    if snt < nosnt: return 0
    else: return 1
for i in range(int(input())):
    n = input()
    if solve(n): print("YES")
    else: print("NO")