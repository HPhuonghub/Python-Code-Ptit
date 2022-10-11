import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def out(self):
        tus = self.tu // math.gcd(self.tu, self.mau)
        maus = self.mau // math.gcd(self.tu, self.mau)
        print(str(tus) + "/" + str(maus))


a = input().split()
p = PhanSo(int(a[0]), int(a[1]))
p.out()
