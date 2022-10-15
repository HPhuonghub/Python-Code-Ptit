def trans(s) :
    n = 0
    for i in s : n += ord(i) - ord('0')
    return str(n)

s = input()
if len(s)==1: print(1)
else:
    count = 0
    while(len(s) > 1) :
        s = trans(s)
        count += 1
    print(count)