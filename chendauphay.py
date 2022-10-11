a = input()
i = len(a) - 1
dem = 0
s = ""
while 1:
    dem += 1
    s = a[i] + s
    if i == 0:
        break
    if dem == 3:
        s = "," + s
        dem = 0
    i -= 1
print(s)