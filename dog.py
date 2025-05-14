from pets import Pets

class Dog(Pets):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

