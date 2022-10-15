a = int(input())
for i in range(0,a):
    b = input()
    dem = 1
    l = len(b)
    for j in range(0,l-1):
        if b[j] == b[j+1]:
            dem += 1
        else :
            print(dem ,b[j] , sep = "" , end = "")
            dem = 1
    print(dem , b[l-1] , sep="", end="")
    print()