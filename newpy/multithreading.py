from threading import  *
from time import sleep

class Bike(Thread):
    def rin(self):
        for i in range(5):
         print("i like a top torqe bike")
         sleep(2)

class Car(Thread):
    def rin(self):
        for i in range(4):
        sleep(1)

         print("i like a top torqe car")
b1= Bike()
c1 = Car()
print(b1)
print(c1)

b1.rin()
c1.rin()