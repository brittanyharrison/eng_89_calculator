"""

"""


class BasicCal:

    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def add(self):
        return float(self.num1+self.num2)

    def sub(self):
        return float(self.num1 - self.num2)

    def mult(self):
        return float(self.num1 * self.num2)

    def div(self):
        return float(self.num1 / self.num2)

    def operand(self):
        if self.op == "+":
            print(f"Result: {obj.add()}")
        elif self.op == "-":
            print(f"Result: {obj.sub()}")
        elif self.op == "*":
            print(f"Result: {obj.mult()}")
        elif self.op == "+":
            print(f"Result: {obj.add()}")


while True:
    num1 = float(input("First number: "))
    op = input("op")
    num2 = float(input("Second number: "))

    obj = BasicCal(num1, num2, op)
    print(obj.operand())


