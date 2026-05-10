class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"{self.brand} is moving")


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def honk(self):
        print("Beep beep!")


class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def honk(self):
        print("Ring ring!")


car = Car("SUV", 4)
bike = Bike("Tri", 2)

car.move()    # SUV is moving
bike.move()   # Tri is moving
car.honk()    # Beep beep!
bike.honk()   # Ring ring!

