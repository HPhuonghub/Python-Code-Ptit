import math
def nghich(n):
    s=0
    while n>0:
        h=n%10
        s = s*10 + h
        n=n//10
    return s
for i in range(int(input())):
    m = int(input())
    if math.gcd(m, nghich(m))==1:
        print("YES")
    else:
        print("NO")