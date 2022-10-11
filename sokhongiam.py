a = int(input())
for i in range(0,a):
    dem = 0
    b = input()
    for j in range(0,len(b)-1):
        if int(b[j]) <= int(b[j+1]):
            continue
        else :
            dem = 1
            break
    if dem == 0 :
        print("YES")
    else :
        print("NO")