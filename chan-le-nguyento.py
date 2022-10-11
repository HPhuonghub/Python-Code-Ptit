def nt(n):
    if n<2: return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0: return 0
        return 1
def solve(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if (i % 2) != (int(s[i]) % 2) : return 0
    if nt(sum): return 1
    else: return 0
for i in range(int(input())):
    n = input()
    if solve(n): print("YES")
    else: print("NO")