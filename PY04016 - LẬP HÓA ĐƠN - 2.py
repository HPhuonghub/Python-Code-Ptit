from datetime import datetime
idphong = [25, 34, 50, 80]


class KhachHang:
    def __init__(self, id, name, phong, ngayDen, ngayDi, phi):
        self.id = id
        self.name = name
        self.phong = phong
        self.ngayO = str(datetime.strptime(ngayDi, '%d/%m/%Y') -
                         datetime.strptime(ngayDen, '%d/%m/%Y')).split()[0]
        if self.ngayO == '0:00:00':
            self.ngayO = 1
        else:
            self.ngayO = int(self.ngayO) + 1
        self.phi = phi
        self.tong = idphong[int(self.phong[0])-1] * self.ngayO + self.phi

    def __str__(self):
        return self.id + " " + self.name + " " + self.phong + " " + str(self.ngayO) + " " + str(self.tong)


list1 = []
for i in range(int(input())):
    id = i + 1
    list1.append(KhachHang('KH%02d' % id, input().strip(), input().strip(),
                 input().strip(), input().strip(), int(input())))
list1 = sorted(list1, key=lambda x: - x.tong)
for i in list1:
    print(i)
