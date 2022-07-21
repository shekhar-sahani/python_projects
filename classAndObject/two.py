class Computer:

    def __init__(self, model, ram):
        self.model_name = model
        self.ram = ram
    
    def config(self):
        print('model is', self.model_name, 'and ram is', self.ram)


com1 = Computer('acer', '8gb')
com2 = Computer('dell', '4gb')



com1.config()
com2.config()

