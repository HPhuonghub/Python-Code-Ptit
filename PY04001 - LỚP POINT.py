import math
from decimal import Decimal


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, a):
        x1 = self.x - a.x
        y1 = self.y - a.y
        h = math.sqrt(pow(x1, 2)+pow(y1, 2))
        return "{:.4f}".format(h)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
