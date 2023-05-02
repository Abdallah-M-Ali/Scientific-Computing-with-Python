
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        W = self.width
        H = self.height
        if H > 50 or W > 50:
            return "Too big for picture."
        picture = ""
        for i in range (H):
            picture += "*" * W + "\n"
            # for j in range (H):
            #     picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_dide(self, side):
        self.width = side
        self.height = side
        return self.width, self.height

    def set_width(self, width):
        self.width = width
        self.height = width
        return self.width, self.height

    def set_height(self, height):
        self.width = height
        self.height = height
        return self.width, self.height

    def __str__(self):
        return f"Square(side={self.width})"

p1 = Rectangle(5, 10)
p1.set_width(4)
p1.set_height(8)

p2 = Rectangle(20, 30)
p2.set_width(4)
p2.set_height(4)

print(p1.get_amount_inside(p2))

print(p1)
print(p1.get_picture())

s1 = Square(2)
s1.set_height(3)
s1.set_dide(20)

print(s1)
print(s1.get_amount_inside(p1))
print(s1.get_picture())


