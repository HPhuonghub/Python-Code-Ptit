for i in range(int(input())):
    s = input()
    sum = 0
    a = []
    for i in range(len(s)):
        if (s[i] >= '0' and s[i] <= '9'):
            sum += int(s[i])
        else:
            a.append(s[i])
    a.sort()
    for i in a:
        print(i, end="")
    print(sum)
