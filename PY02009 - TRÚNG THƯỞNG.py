
for i in range(int(input())):
    m = {}
    for i in range(int(input())):
        x = int(input())
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
    count = 0
    for i in m:
        if m[i] > count:
            count = m[i]
            p = i
        elif m[i] == count:
            p = min(p, i)
    print(p)
