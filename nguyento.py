import math
def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0: return 0
        return 1
for i in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            count += 1
    if nt(count) == 1:
        print("YES")
    else :
        print("NO")