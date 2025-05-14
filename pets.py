class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Pet {self.name} {self.age} year old'