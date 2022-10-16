import math

n = int(input())
a = sorted([int(i) for i in input().split()])
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if math.gcd(a[i], a[j]) == 1:
            print(str(a[i]) + " " + str(a[j]))
