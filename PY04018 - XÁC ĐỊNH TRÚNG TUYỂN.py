class GiangVien:
    def __init__(self, id, name, ma, tin, cm):
        self.id = id
        self.name = name
        self.ma = ma
        self.tin = tin
        self.cm = cm
        self.tong = self.tin * 2 + self.cm

        if self.ma[1] == '1':
            self.tong += 2
        elif self.ma[1] == '2':
            self.tong += 1.5
        elif self.ma[1] == '3':
            self.tong += 1
        else:
            self.tong += 0

        if self.ma[0] == 'A':
            self.mon = "TOAN"
        elif self.ma[0] == 'B':
            self.mon = "LY"
        else:
            self.mon = "HOA"

        if self.tong >= 18:
            self.xh = "TRUNG TUYEN"
        else:
            self.xh = "LOAI"

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + self.mon + ' ' + '{:.1f}'.format(self.tong) + ' ' + self.xh


a = []
for i in range(int(input())):
    a.append(GiangVien('GV%02d' % (i+1), input(),
             input(), float(input()), float(input())))
a = sorted(a, key=lambda x: -x.tong)
for i in a:
    print(i)
