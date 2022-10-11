a =int(input())
for i in range(0,a):
    b = input()
    tich = 1
    for j in range(0,len(b)):
        if b[j] != "0":
            tich = tich * int(b[j])
    print(tich)