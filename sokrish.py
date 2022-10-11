def gt(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
def solve(n):
    m = n
    s = 0
    while m>0:
        h = m % 10
        s += gt(h)
        m = m//10
    if s==n: print("Yes")
    else: print("No")
for i in range(int(input())):
    n = int(input())
    solve(n)