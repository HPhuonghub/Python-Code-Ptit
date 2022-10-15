a = int(input())
for i in range(0,a):
    b = input()
    count = 0
    for j in range(0,len(b)):
        if b[j] == "0" or b[j] == "1" or b[j] == "2":
            continue
        else :
            count = 1
            break
    if count == 1:
        print("NO")
    else :
        print("YES")