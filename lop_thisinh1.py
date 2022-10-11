class ThiSinh:
    def __init__(self, ten, sn, diem1, diem2, diem3):
        self.ten = ten
        self.sn = sn
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3

    def out(self):
        print(self.ten + " " + self.sn + " " +
              "{:.1f}".format(self.diem1 + self.diem2 + self.diem3))


ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
ts.out()
