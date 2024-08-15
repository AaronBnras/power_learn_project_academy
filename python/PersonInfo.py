class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

name = input("Enter the person's name: ")
age = input("Enter the person's age: ")
gender = input("Enter the person's gender: ")

person_instance = Person(name=name, age=age, gender=gender)

person_instance.introduce()
