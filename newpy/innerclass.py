class Abhijith:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.borderr = self.Border()

    def border(self):
        print(self.name, self.home)
        self.borderr.border()

    class Border:

        def __init__(self):
            self.tamilnadu = 'malayadi'
            self.kerala = 'parashala'

        def border(self):
            print(self.tamilnadu, self.kerala)


a1 = Abhijith('Abhijith', 'malaydi')
a1.border()
