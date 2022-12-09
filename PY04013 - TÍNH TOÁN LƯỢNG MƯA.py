def time(a, b):
    return b[0] * 60 + b[1] - a[0] * 60 - a[1]


list1 = {}
for i in range(int(input())):
    name = input()
    a = [int(x) for x in input().split(':')]
    b = [int(x) for x in input().split(':')]
    luongMua = int(input())
    if name not in list1:
        list1[name] = (time(a, b), luongMua)
    else:
        list1[name] = (list1[name][0] + time(a, b), list1[name][1] + luongMua)
t = 1
for i in list1:
    print('T{:02d}'.format(t), i, '{:.2f}'.format(
        list1[i][1] * 60 / list1[i][0]))
    t += 1
