class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3 

    def get_m2(self):
        return self.m2

    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
         print('This is student class')


s1 = Student(49, 78, 90)
s2 = Student(43, 28, 50)

# print(s2.get_m2())
Student.info()
