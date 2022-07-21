class Car:

    wheels = 4     # Class Variables

    def __init__(self):
        self.mil = 10               # Instance Variables
        self.company = 'audi'


c1 = Car()
c2 = Car()

Car.wheels = 5



c1.mil = 8


print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)



