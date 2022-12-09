class HoaDon:
    def __init__(self, name, cu, moi, id):
        self.name = name
        self.cu = cu
        self.moi = moi
        self.id = id
        self.tong = 0

    def gettong(self):
        s = self.moi - self.cu
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.tong = round(s)

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + str(self.tong)


list1 = []
for i in range(int(input())):
    name = input()
    cu = int(input())
    moi = int(input())
    id = i + 1
    list1.append(HoaDon(name, cu, moi, 'KH%02d' % id))
for i in list1:
    i.gettong()
list1 = sorted(list1, key=lambda x: x.tong, reverse=True)
for i in list1:
    print(i)
