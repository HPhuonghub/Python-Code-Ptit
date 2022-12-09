class NhanVien:
    def __init__(self, name, a, b, id):
        self.name = name
        self.id = id
        if a > 10:
            a /= 10
        if b > 10:
            b /= 10
        self.d = (a + b) / 2
        if self.d < 5:
            self.l = 'TRUOT'
        elif self.d < 8:
            self.l = 'CAN NHAC'
        elif self.d < 9.5:
            self.l = 'DAT'
        else:
            self.l = 'XUAT SAC'

    def output(self):
        print(self.id, self.name, '{:.2f}'.format(self.d), self.l)


list1 = []
for i in range(int(input())):
    name = input()
    a = float(input())
    b = float(input())
    id = i + 1
    list1.append(NhanVien(name, a, b, 'TS0' + str(id)))
list1 = sorted(list1, key=lambda x: x.d, reverse=True)
for i in list1:
    i.output()
