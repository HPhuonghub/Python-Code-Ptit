def tn(n):
    n = str(n)
    a = [int(i) for i in n]
    b=a.copy();b.reverse()
    if a==b: print("YES")
    else: print("NO")
for i in range(int(input())):
    n = input()
    s = 0
    for j in range(len(n)):
        s = s + int(n[j])
    if s<10: print("NO")
    else: tn(s)