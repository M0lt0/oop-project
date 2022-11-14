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


first_student = Student("body", 24, ["numerical methods", "signal"])
sec_student = Student("body", 24, ["analog", "wave"])

sec_student.describe_Me()
first_student.is_old(20)
