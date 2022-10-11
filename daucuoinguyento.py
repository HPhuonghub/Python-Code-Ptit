def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        return 1
def check(n):
    sum1 = 0
    sum2 = 0
    for i in range(0,3):
        s = int(n[len(n)-3+i])
        sum1 = sum1*10 + s
    for i in range(0,3):
        s = int(n[i])
        sum2 = sum2*10 + s
    if nt(sum1) and nt(sum2): return 1
    else: return 0
for i in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")