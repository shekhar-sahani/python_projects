class Computer:
    def __init__(self):
        self.name = 'shekhar'
        self.age = 20

    def update(self):
        self.age = 19

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()


c1.name = 'starlord'
c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):
    print('age is same')
else:
    print('age is not same')
