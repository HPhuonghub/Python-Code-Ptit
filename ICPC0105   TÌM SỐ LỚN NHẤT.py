for i in range(int(input())):
    a = input()
    a = a + 'z'
    mins = -10**20
    s = 0
    for i in range(len(a)):
        if a[i].isalpha():
            if i!=0 and a[i-1].isdigit(): mins = max(mins,s)
            s = 0
        else :
            s = s*10 + int(a[i])
    print(mins)