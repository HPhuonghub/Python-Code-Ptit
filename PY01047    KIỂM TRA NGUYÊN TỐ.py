def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        return 1
def check(n):
    sum = 0
    for i in range(0,4):
        s = int(n[len(n)-4+i])
        sum = sum*10 + s
    if nt(sum): return 1
    else: return 0
for i in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")