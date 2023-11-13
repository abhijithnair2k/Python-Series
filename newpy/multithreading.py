from threading import  *
from time import sleep

class Bike(Thread):
    def run(self):
      for i in range(5):
           print("i like a top toruqe bike")
           sleep(2)

class Car(Thread):
    def run(self):
      for i in range(4):
           print("i like a top toruqe car")
           sleep(1)

b1= Bike()
c1 = Car()

b1.start()
sleep(1)
c1.start()
print("bye")

b1.join()
c1.join()