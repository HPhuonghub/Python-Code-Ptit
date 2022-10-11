def solve(n):
    sum = 0
    tich = 1
    dem = 0
    for i in range(len(n)):
        if i%2==0: sum += int(n[i])
        else:
            if n[i]!='0':
                tich *= int(n[i])
                dem = 1
    if dem == 0: tich = 0
    print(sum, tich)
for i in range(int(input())):
    n = input()
    solve(n)