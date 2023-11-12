class Computer:
    def config(self):
        print('dell')
com1= Computer()
com1.config()

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print('dell has ', self.cpu,self.ram)
com1= Computer( 'i5',16)
com1.config()


