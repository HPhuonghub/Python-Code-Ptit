import math
def snt(n):
    if n<2: return 0
    else :
        for i in range(2,int(n**0.5)+1):
            if n % i == 0: return 0
        return 1
for i in range(int(input())):
    a,b = map(int, input().split())
    c = str(math.gcd(a, b))
    s = 0
    for i in c:
        s += int(i)
    if snt(s)==1 : print("YES")
    else : print("NO")