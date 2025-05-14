from pets import Pets

class Cat(Pets):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color