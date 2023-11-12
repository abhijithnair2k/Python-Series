# num = [1,3,45,67,]
# nums = iter(num)
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# print(next(nums))
##########################
class Itertor:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <=10:
            val=self.num
            self.num +=1
            return val

value= Itertor()
print(value.__next__())
print(value.__next__())



