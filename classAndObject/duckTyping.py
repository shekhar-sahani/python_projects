class VsCode:
    def execute(self):
        print('Compiling')
        print('running')

class MyEditor:
    def execute(self):
        print('Spell Check')
        print('Compiling')
        print('running')


class Laptops:
    def code(self, ide):
        ide.execute()

ide = MyEditor()
lap1 = Laptops()

lap1.code(ide)

