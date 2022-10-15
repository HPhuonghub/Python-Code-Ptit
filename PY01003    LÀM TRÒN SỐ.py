for i in range(int(input())):
    a = input()
    dem = len(a) - 1
    if int(a) <= 10: print(a)
    else:
        s = 0
        t = 0
        while dem >= 0:
            if dem == 0:
                if t==1:
                    m = int(a[dem]) + 1
                    s=m * pow(10,len(a)-1)
                else:
                    m = int(a[dem])
                    s = m * pow(10,len(a)-1)
                break
            else:
                if int(a[dem]) + t > 4:
                    t = 1
                else:
                    t = 0
            dem -= 1
        print(s)