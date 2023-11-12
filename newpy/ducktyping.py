class Battery:
    def battery(self):
        print("litjium ion")


class Car:
    def battery(self):
        print("ion battery")
class Tata:
    def manu(self,bat):
      bat.battery()

bat=Battery()
t1=Tata()
t1.manu(bat)

# c1 = Car()
# c1.battery()
