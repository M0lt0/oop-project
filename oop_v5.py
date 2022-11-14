
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"first name is {self.name} and the age is {self.age}"


class Man(Person):
    gender = "male"
    n_of_men = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.n_of_men += 1

    def display(self):
        string = super().display()
        return string + f" and voice is {self.voice} and gender is {self.gender}"


class Woman(Person):
    gender = "female"
    n_of_women = 0

    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Woman.n_of_women += 1

    def display(self):
        string = super().display()
        return string + f" and hair is {self.hair} and gender is {self.gender}"


women = Woman("shahed", 24, "straight")
print(women.display())
print(Woman.n_of_women)
