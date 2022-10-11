class Rectangle():
    def __init__(self, h, w, colors):
        self.h = h
        self.w = w
        self.colors = colors

    def perimeter(self):
        return (self.h + self.w)*2

    def area(self):
        return self.h*self.w

    def color(self):
        self.colors = self.colors.lower()
        solve = self.colors[0:1:].upper() + self.colors[1::]
        return solve


if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    else:
        print("INVALID")
