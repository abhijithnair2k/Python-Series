class Person:
    def __init__(self):
        self.name='Abhijith'
    #     self.phno=9080541
    # # def update(self):
    # #     self.phno=90200
    def compare(self,other):
          if self.name == other.name:
              return True
          else:
              return False

p1=Person()
p2=Person()
p1.name="Ajith"

# p1.update()
print(p1.name)
print(p2.name)


if p1.compare(p2):
  print("they are same")