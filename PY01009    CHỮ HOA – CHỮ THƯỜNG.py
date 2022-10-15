a = str(input())
dem_thuong = 0
dem_hoa = 0
for i in range(0,len(a)):
    if a[i] >= "a" and a[i] <= "z":
        dem_thuong += 1
    else :
        dem_hoa += 1
if dem_hoa <= dem_thuong:
    print(a.lower())
else :
    print(a.upper())