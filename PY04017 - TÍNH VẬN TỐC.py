class ThiSinh:
    def __init__(self, name, diadiem, time):
        self.name = name
        self.diadiem = diadiem
        self.time = time
        a = [i[0] for i in name.split()]
        b = [i[0] for i in diadiem.split()]
        self.id = ''.join(b) + ''.join(a)
        c = time.split(':')
        self.vt = 120 / (int(c[0]) - 6 + int(c[1]) / 60)

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + self.diadiem + ' ' + str(round(self.vt)) + ' Km/h'


a = []
for i in range(int(input())):
    a.append(ThiSinh(input(), input(), input()))
a = sorted(a, key=lambda x: -x.vt)
for i in a:
    print(i)
