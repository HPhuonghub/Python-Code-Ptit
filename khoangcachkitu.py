def check(s):
    n = str(s)
    l = len(n)
    a = list(reversed(n))
    b = ''.join(a)
    for i in range(0,l):
        if abs(ord(n[i])-ord(n[i-1]))!=abs(ord(b[i])-ord(b[i-1])): return 0
    return 1
for i in range(int(input())):
    s = input()
    if check(s)==1: print("YES")
    else: print("NO")