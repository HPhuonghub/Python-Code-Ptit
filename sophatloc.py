a = int(input())
for i in range(0,a):
    b = input()
    if b[len(b)-2] == "8" and b[len(b)-1] == "6":
        print("YES")
    else :
        print("NO")