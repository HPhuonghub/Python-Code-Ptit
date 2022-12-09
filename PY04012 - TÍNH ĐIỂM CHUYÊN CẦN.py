m = {}
t = int(input())
for i in range(t):
    id = input()
    name = input()
    class1 = input()
    m[id] = [name, class1]
for i in range(t):
    id, cc = input().split()
    d = 10
    for j in cc:
        if j == 'm':
            d -= 1
        elif j == 'v':
            d -= 2
        else:
            d -= 0
    if d < 0:
        d = 0
    m[id] = m[id] + [d]
for i in m:
    print(i, end=" ")
    for j in m[i]:
        print(j, end=" ")
    if m[i][-1] == 0:
        print('KDDK')
    else:
        print()
