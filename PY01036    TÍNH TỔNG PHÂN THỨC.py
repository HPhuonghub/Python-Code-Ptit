a = int(input())
for i in range(0,a):
    b = int(input())
    s = 0
    if b % 2 == 0:
        for j in range(2,b+1,2):
            s = s + float(1/j)
    else :
        for j in range(1,b+1,2):
            s = s + float(1/j)
    print("{:.6f}".format(s))