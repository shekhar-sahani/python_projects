class Computer:
    
    def config(self):
        print("15, 16gb, 1Tb")


com1 = Computer()
com2 = Computer()

Computer.config(com1)


com1.config()
com2.config()

