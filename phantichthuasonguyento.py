for i in range(int(input())):
    n = int(input())
    print("1 ", end="")
    for k in range(2,int(n**0.5)+1):
        count=0
        if n%k==0:
            while n%k==0:
                count+=1
                n=n//k
            print("* "+str(k) + "^" +str(count),end=" ")
    if n>1: print("* "+str(n) + "^1",end="")
    print()
