from datetime import date


class Student:
    num = 0

    def __init__(self, name, age, courses):

        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.num += 1

    def describe_Me(self):
        print(f"My name is {self.__name} and i'am {self.__age} years old ")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__name = new_age

    def is_old(self, num):
        if self.age <= num:
            print("this person is not old ")
        else:
            print("this person is old ")


""" first_student = Student("body", 24, ["numerical methods", "signal"])
sec_student = Student("body", 24, ["analog", "wave"])

sec_student.describe_Me()
first_student.is_old(20) """

# class creation


class Student:
    def __init__(self, name, age=0, courses="none"):
        self.__name = name
        self.__age = age

    def describe(self):
        print(f"my name is {self.__name} , iam {self.__age} years old")

    @classmethod
    def initFromBirthYear(cls, name, birth):
        return cls(name, date.today().year - birth)


class Pizza:
    def __init__(self, ingrd):
        self.ingrd = ingrd

    @classmethod
    def veg(cls):
        return cls(["tomatos", "olives", ])

    @classmethod
    def mrgt(cls):
        return cls(["meat", "olives", ])

    def __str__(self):
        return f"Pizza ingredient are {self.ingrd} "


pizza_veg = Pizza(["cucamber", "chille"])
pizza_me = Pizza.veg()

print(pizza_veg, pizza_me)


# static methods
