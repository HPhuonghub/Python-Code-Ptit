m = {}
n, k = [int(x) for x in input().split()]
for i in range(n):
    t = input()
    s = ''
    for j in t.lower() + ' ':
        if (j >= 'a' and j <= 'z') or (j >= '0' and j <= '9'):
            s += j
        else:
            if s != '':
                if s in m:
                    m[s] += 1
                else:
                    m[s] = 1
            s = ''
m = sorted(m.items(), key=lambda x: (-x[-1], x[0]))
for i in m:
    if i[1] >= k:
        print(i[0], i[1])
