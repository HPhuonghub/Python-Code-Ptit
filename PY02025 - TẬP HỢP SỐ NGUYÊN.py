n, m = [int(x) for x in input().split()]
a = sorted(set([int(x) for x in input().split()]))
b = sorted(set([int(x) for x in input().split()]))
for i in a:
    if i in b:
        print(i, end=" ")
print()
for i in a:
    if i not in b:
        print(i, end=" ")
print()
for i in b:
    if i not in a:
        print(i, end=" ")
