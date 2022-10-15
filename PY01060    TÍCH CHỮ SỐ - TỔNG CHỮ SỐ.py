def solve(n):
    sum = 0
    tich = 1
    for i in range(len(n)):
        if i%2!=0: sum += int(n[i])
        else:
            if n[i]!='0':
                tich *= int(n[i])
    print(tich, sum)
for i in range(int(input())):
    n = input()
    solve(n)