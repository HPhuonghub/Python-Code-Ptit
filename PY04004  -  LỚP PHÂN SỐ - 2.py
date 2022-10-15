import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def out(self, q):
        tu1 = self.tu * q.mau + self.mau * q.tu
        mau1 = self.mau * q.mau
        tus = tu1 // math.gcd(tu1, mau1)
        maus = mau1 // math.gcd(tu1, mau1)
        print(str(tus) + "/" + str(maus))


a = input().split()
p = PhanSo(int(a[0]), int(a[1]))
q = PhanSo(int(a[2]), int(a[3]))
p.out(q)
