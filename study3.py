# Question 2 — Medium
# Create a parent class Shape with a private attribute __color with getter and setter (valid colors: "red", "blue", "green"). Child class Circle adds radius and method describe() that prints "A <color> circle with radius <radius>".

class Shape:
    def __init__(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, valid):
        if valid in ["red", "blue", "green"]:
            self.__color = valid
        else:
            print("Invalid color. Valid colors are: red, blue, green.")   

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def describe(self):
        print(f"A {self.color} circle with radius {self.radius}")

circle1 = Circle("red", 5)
circle1.describe()
circle2 = Circle("blue", 3)
circle2.color = "blue"
circle2.describe()
circle3 = Circle("green", 7)
circle3.color = "yellow"  # Invalid color
circle3.describe()
