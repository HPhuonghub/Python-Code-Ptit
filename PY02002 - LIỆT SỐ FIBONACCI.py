def fibo(n):
    f1 = 1
    f2 = 1
    fn = 0
    if n<3:
        fn = 1
    else:
        for i in range(1,n-1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
    return fn
for i in range(int(input())):
    n,k = [int(i) for i in input().split()]
    for j in range(n,k+1):
        print(fibo(j), end=" ")
    print()
        