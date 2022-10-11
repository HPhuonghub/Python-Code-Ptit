a, k, n = [int(i) for i in input().split()]
m = int(n/k) + 1
dem = 0
for i in range(1,m):
    x = i*k-a
    if x > 0:
        print(x, end=" ")
        dem = 1
if dem == 0:
    print(-1)