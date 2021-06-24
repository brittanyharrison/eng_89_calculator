from calculator import BasicCal
import math
"""
"""

class FuncCal(BasicCal):
    def __init__(self):
        super().__init__()

    def area_of_circle(self, radius):
        radius = float(input("What is the radius"))
        return (radius * radius) * math.pi

    def area_of_square(self):
        height = float(input("What is the height"))
        length = float(input("What is the length"))
        return (length * height)

    def area_of_triangle(self):
        return(height * width) * 2

    def area(self):
        if user_prompt == "circle":
            return obj2.area_of_circle()
        elif user_prompt == "square":
            return obj2.area_of_square()
        else user_prompt == "triangle":
            return obj2.area_of_triangle()
obj2 = FuncCal
user_prompt = input("What would you like to calculate?")
    radius = float(input("What is the radius"))
    while True:


        if user_prompt == "circle":
            radius = float(input("What is the radius"))
            return
            radius = float(input("Whats the radius"))
    height = float(input("What is the height?"))
    length =


