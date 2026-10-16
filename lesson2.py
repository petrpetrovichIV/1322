import random

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = 1
        self.money = 100

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        print(f"Skills: {self.skills}")
        print(f"Money: ${self.money}")

    def study(self):
        self.skills += 1
        print("Time to study 🧑‍🎓📚")

    def chill(self):
        self.skills -= 0.5
        self.money -= random.randint(25,100)
        print("Chilling ... 😎🍵")

    def work(self):
        self.skills += 0.5
        self.money += 50 + random.randint(0,50)
        print("Hard working ... 👷‍♂️💪")

# john = Student('John', 13)
# john.info()

alex = Student('Alex', 12)
alex.info()

for day in range(366):
    alex_choice = random.randint(1, 3)

    if alex_choice == 1:
        alex.study()
    elif alex_choice == 2:
        alex.chill()
    else:
        alex.work()

alex.age += 1
alex.info()