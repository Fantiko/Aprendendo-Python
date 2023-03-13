#   Programaçao orientada a objetos

class Dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


d = Dog('dory', 3)
print(d.get_name())

