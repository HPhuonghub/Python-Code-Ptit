n = int((input()))
a = sorted([float(i) for i in input().split()])
sum = 0
x1 = a[0]
x2 = a[n-1]
dem = 0
for i in a:
    if i != x1 and i != x2:
        sum += i
        dem += 1
sum = sum / dem
print("{:.2f}".format(sum))
