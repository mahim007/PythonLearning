class Person:
    def __init__(self, name, age, email):
        super().__init__()
        self.name = name
        self.age = age
        self.email = email
    
    def getInfo(self):
        print(f"hi i am {self.name}, {self.age}, {self.email}")


mahim = Person("mahim", 25, "mahim@gmail.com")
mahim.getInfo()