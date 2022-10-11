def nt(n):
    if n<2: return 0
    else: 
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return 0
        return 1
def check(n):
    count1 = 0
    count2 = 0
    for i in range(0,len(n)):
        m = int(n[i])
        if nt(m): count1 += 1
        else: count2 += 1
    if count1 > count2: return True
    else: return False
for i in range(int(input())):
    n = input()
    if check(n) and nt(len(n)): print("YES")
    else: print("NO")