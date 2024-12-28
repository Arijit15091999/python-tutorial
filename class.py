class MyClass:
    x = 5

obj = MyClass()

print(obj.x)

class Person:
    def __init__(self, name, age, phoneNumber = "abc"):
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.name}({self.age})(phoneNumber:- {self.phoneNumber})"

person = Person(name = "Arijit", age = 24)

print(person)

class Student(Person):
    def __init__(self, name, age, year, phoneNumber = 123):
        super().__init__(name, age, phoneNumber)
        self.year = year

student = Student(name = "Arijit", age = 24, year = 1999)

print(student)