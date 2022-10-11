class SoPhuc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def out(self, k):
        a = self.x + k.x
        b = self.y + k.y
        c = a * self.x - b * self.y
        d = b * self.x + a * self.y
        e = a * a - b * b
        f = 2 * a * b
        print(c, end=" ")
        if d < 0:
            print("- " + str(abs(d)) + "i, ", end="")
        else:
            print("+ " + str(d) + "i, ", end="")
        print(e, end=" ")
        if f < 0:
            print("- " + str(abs(f)) + "i ", end="")
        else:
            print("+ " + str(f) + "i", end="")
        print()


t = int(input())
while t > 0:
    a = [int(i) for i in input().split()]
    b = SoPhuc(a[0], a[1])
    c = SoPhuc(a[2], a[3])
    b.out(c)
    t -= 1
