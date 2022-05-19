from classObject import Calculator


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getAllData(self):
        return self.num2 + self.num + self.Sum()


obj = ChildImp()
print(obj.getAllData())
