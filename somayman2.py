a = int(input())
for i in range(0,a):
    b = input()
    dem = 0
    for i in range(0, len(b)):
        if b[i] == "4":
            dem = dem + 1
        if b[i] == "7":
            dem = dem + 1
    if dem == len(b):
        print("YES")
    else:
        print("NO")
