a = int(input())
for i in range(0,a):
    b = input()
    dem = 0
    for j in range(2,len(b)):
        if b[j] == b[j-2]:
            continue
        else :
            dem = 1
            break
    if dem == 0:
        print("YES")
    else :
        print("NO") 