a =int(input())
for i in range(0,a):
    b = input()
    tong = 0
    for j in range(0,len(b)):
        tong = tong + int(b[j])
    if tong % 3 == 0:
        print("YES")
    else :
        print("NO")