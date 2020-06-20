class Mammal:
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def walk(self):
        print(f"{self.name} walks")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} barks")

class Cat(Mammal):
    def meow(self):
        print(f"{self.name} meows")

dog = Dog("burno")
dog.walk()
dog.bark()

cat = Cat("mini")
cat.walk()
cat.meow()

