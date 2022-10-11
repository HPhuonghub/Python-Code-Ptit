size = 0
b = set()
while True:
    a = [int(i) for i in input().split()]
    size += len(a)
    count = 0
    for i in a:
        h = i % 42
        b.add(h)
    if size == 10:
        break
print(len(b))
