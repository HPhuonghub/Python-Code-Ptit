def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        return 1
def solve(n):
    if nt(n)!=1: return 0
    m = int(str(n)[::-1])
    if nt(m)!=1: return 0
    while n>0:
        h = n%10
        if nt(h)!=1: return 0
        n = n//10
    return 1
for i in range(int(input())):
    n = int(input())
    if solve(n): print("Yes")
    else: print("No")