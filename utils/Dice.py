import random

class Dice:
    def __init__(self):
        self.dice1 = 6
        self.dice2 = 6
    
    def roll(self):
        random_number1 = random.randint(1, self.dice1)
        random_number2 = random.randint(2, self.dice2)
        return [random_number1, random_number2]