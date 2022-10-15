a = input()
dem = 0
for i in range (0,len(a)):
    if a[i] == "4":
        dem = dem + 1
    if a[i] == "7":
        dem = dem + 1
if dem == 4:
    print("YES")
elif dem == 7:
    print("YES")
else:
    print("NO")