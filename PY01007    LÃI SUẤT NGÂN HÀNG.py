import math
for i in range(int(input())):
    n,x,m = [float(i) for i in input().split()]
    y = math.log(m/n,1+x/100)
    if y == int(y): print(y)
    else : print(int(y)+1)