def nt(n):
    if n<2: return 0
    else: 
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        return 1
def check(n):
    for i in range(len(n)):
        if nt(i) != nt(int(n[i])): return 0
    return 1
for i in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")