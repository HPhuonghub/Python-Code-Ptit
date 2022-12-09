import math


class SinhVien:
    def __init__(self, name, a, id):
        self.name = name
        self.a = a
        self.id = id
        self.tb = 0
        self.xh = ""

    def diemtb(self):
        sum = dem = 0
        for i in self.a:
            if dem <= 1:
                sum += i*2
            else:
                sum += i
            dem += 1
        self.tb = round(sum / 10 / 1.2, 1)

    def xephang(self):
        if self.tb >= 9:
            self.xh = "XUAT SAC"
        elif self.tb >= 8:
            self.xh = "GIOI"
        elif self.tb >= 7:
            self.xh = "KHA"
        elif self.tb >= 5:
            self.xh = "TB"
        else:
            self.xh = "YEU"

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + ('%.1f' % self.tb) + ' ' + self.xh


lists = []
for i in range(int(input())):
    name = input()
    a = [float(x) for x in input().split()]
    id = i+1
    lists.append(SinhVien(name, a, "HS%02d" % id))
for i in lists:
    i.diemtb()
    i.xephang()
lists = sorted(lists, key=lambda x: x.tb, reverse=True)
for i in lists:
    print(i)
