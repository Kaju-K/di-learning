from copy import deepcopy
import math

class Circle:
    number = 1
    def __init__(self) -> None:
        self.name = str(Circle.number)
        print(f"This is circle {Circle.number}")
        while True:
            self.answer = input("Which value do you want to put, radius or diameter? ")
            if (self.answer != "radius") and (self.answer != "diameter"):
                continue
            self.value = int(input(f"What's the value for the {self.answer}? "))
            if self.answer == "radius":
                self.radius = self.value
                self.diameter = self.value*2
            else:
                self.radius = self.value/2
                self.diameter = self.value
            break
        self.area = math.pi*(self.radius**2)
        Circle.number += 1

    def __repr__(self) -> str:
        return f"Circle {self.name}"

    def __str__(self):
        if self.radius > 5:
            return "O"
        return "o"
    
    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        return False
    
    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        return False
    
    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        return False
    
    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        return False
    
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False

    def __add__(self, other):
        another_circle = deepcopy(self)
        another_circle.name = Circle.number
        another_circle.radius = self.radius + other.radius
        another_circle.diameter = another_circle.radius*2
        another_circle.area = another_circle.radius**2*math.pi
        Circle.number += 1

        return another_circle


a = Circle()
b = Circle()
