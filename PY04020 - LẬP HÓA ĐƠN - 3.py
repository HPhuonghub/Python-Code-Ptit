class DonHang:
    def __init__(self, id, name, soluong, dongia, chietkhau):
        self.id = id
        self.name = name
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tong = self.dongia * self.soluong - self.chietkhau

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + str(self.soluong) + ' ' + str(self.dongia) + ' ' + str(self.chietkhau) + ' ' + str(self.tong)


a = []
for i in range(int(input())):
    id = i + 1
    a.append(DonHang(input(), input(),
             int(input()), int(input()), int(input())))
a = sorted(a, key=lambda x: -x.tong)
for i in a:
    print(i)
