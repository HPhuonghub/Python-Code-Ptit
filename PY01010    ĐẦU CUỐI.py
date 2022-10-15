a = int(input())
for i in range(0, a):
    b = input()
    if b[0] == b[len(b)-2] and b[1] == b[len(b)-1]:
        print("YES")
    else:
        print("NO")
