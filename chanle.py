import math
def chiahet(s):
    sum = 0
    while(s>0):
        m = s%10
        s = int(s/10)
        sum += m
    if(sum%10==0): return True
    else: return False
def chan(s):
    while(s>10):
        m = s%10
        s = int(s/10)
        h = s%10
        if int(abs(m-h))!=2: return False
        else: return True
for i in range(int(input())):
    s = int(input())
    chan(s)
    if(chiahet(s) and chan(s)): print("YES")
    else: print("NO")