def check(n):
    if len(n)%2==0: return 0
    if n[0]==n[1]: return 0
    if n[0]!=n[len(n)-1]: return 0
    for i in range(2,len(n),2):
        if n[0]!=n[i]: return 0
    return 1
for i in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")