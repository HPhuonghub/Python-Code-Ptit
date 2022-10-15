def check(n):
    if len(n)<2: return 0
    max = 0
    vitri = 0
    for i in range(len(n)):
        if max < int(n[i]):
            max = int(n[i])
            vitri = i
    for i in range(vitri):
        if n[i] < n[i+1]: continue
        else: return 0
    for i in range(vitri,len(n)-1):
        if n[i] > n[i+1]: continue
        else: return 0
    return 1
for i in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")