for i in range(int(input())):
    s1 = sorted(input())
    s2 = sorted(input())
    print("Test " + str(i+1) + ": ", end="")
    if s1 == s2:
        print("YES")
    else:
        print("NO")
