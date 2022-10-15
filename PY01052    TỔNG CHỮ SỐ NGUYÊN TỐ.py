def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        else: return 1
for i in range(int(input())):
    n = input()
    m = 0
    for j in range(len(n)):
        m = m + int(n[j])
    if nt(m)==1: print("YES")
    else: print("NO")