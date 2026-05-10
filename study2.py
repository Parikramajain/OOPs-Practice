# Question 1 — Easy
# Create a parent class Person with name and age, and a child class Employee with extra attribute salary and method show_details() that prints all three.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

object1 = Employee("Alice", 30, 50000)  
object1.show_details()
object2 = Employee("Bob", 25, 45000)
object2.show_details()      
object3 = Employee("Charlie", 35, 60000)
object3.show_details()

# __str__ is a built-in Python method — works automatically whenever Python needs to print or convert your object to a string:


