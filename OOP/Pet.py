class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know what i say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old an i am {self.color} color")


class Dog(Pet):
    def speak(self):
        print("au au")


p = Pet("bob", 22)
p.show()
c = Cat("Mia", 8, "white")
c.show()
d = Dog("sheik", 15)
d.show()
