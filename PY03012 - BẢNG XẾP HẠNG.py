import functools


class SinhVien:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit


def cmp(a, b):
    if a.ac < b.ac:
        return 1
    elif a.ac == b.ac:
        if a.submit > b.submit:
            return 1
        elif a.submit == b.submit:
            if a.name > b.name:
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1


a = []
for i in range(int(input())):
    name = input()
    ac, submit = [int(j) for j in input().split()]
    a.append(SinhVien(name, ac, submit))
a = sorted(a, key=functools.cmp_to_key(cmp))
for i in a:
    print(i.name, i.ac, i.submit)
