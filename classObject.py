class Calculator:
    num = 100

    def __init__(self, a, b):
        self.first = a
        self.second = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I'm now executing method in class")

    def Sum(self):
        return self.first + self.second + Calculator.num


obj = Calculator(1, 2)
obj.getData()
print(obj.Sum())


obj1 = Calculator(3, 4)
obj1.getData()
print(obj1.Sum())

