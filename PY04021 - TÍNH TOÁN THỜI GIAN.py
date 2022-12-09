class Gamer:
    def __init__(self, name, id, gioVao, gioRa):
        self.name = name
        self.id = id
        self.time = gioRa[0]*60 + gioRa[1] - gioVao[0]*60 - gioVao[1]

    def output(self):
        print(self.id, self.name, int(self.time / 60),
              'gio', int(self.time % 60), 'phut')


list1 = []
for i in range(int(input())):
    id = input()
    name = input()
    gioVao = [int(x) for x in input().split(':')]
    gioRa = [int(x) for x in input().split(':')]
    list1.append(Gamer(name, id, gioVao, gioRa))
list1 = sorted(list1, key=lambda x: x.time, reverse=True)
for i in list1:
    i.output()
