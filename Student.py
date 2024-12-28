class Student:
    __numberOfStudents = 0

    def __init__(self, name, rollNumber, marks):
        self.name = name
        self.rollNumber = rollNumber
        self.__marks = marks
        Student.__numberOfStudents += 1

    def getMarks(self):
        return self.__marks
    def setMarks(self, newMarks):
        self.__marks = newMarks

    @staticmethod
    def getNumberOfStudents():
        return Student.__numberOfStudents