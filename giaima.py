a = int(input())
for i in range(0,a):
    b = input()
    s = ""
    for j in range(0,len(b),2):
        for m in range(0,int(b[j+1])):
            s = s + b[j]
    print(s)