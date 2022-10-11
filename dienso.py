for i in range(int(input())):
    n = int(input())
    a = set([int(i) for i in input().split()])
    mins = min(a)
    maxs = max(a)
    print((maxs - mins+1)-len(a))