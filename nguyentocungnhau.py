import math
n, k = [int(i) for i in input().split()]
j = 0
for i in range(pow(10, k-1),pow(10, k)):
    if math.gcd(n, i)==1:
        print(i, end=" ")
        j += 1
    if j==10:
        print("\n")
        j = 0
  
 