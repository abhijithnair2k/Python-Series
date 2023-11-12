from builtins import print

from numpy import *
arr1=array([1,4,6,8])

print(arr1)
print(arr1.dtype)



arr2=array([1,4,6,8.0])

print(arr2)
print(arr2.dtype)


arr1=array([1,4,6,8],float)#we can make the array as float by indicating float on end its optionaal

print(arr1)
print(arr1.dtype)

arr3=linspace(0,8,11) #starting point ,ending point , no of parts that has to be divided
print(arr3)#like 0 to 8 we are dividing it in to 11 parts


arr4=arange(1,9,3)# here th last will indicate the parts between it
print(arr4)


arr5=logspace(2,30,6)
print(arr5)


arr6=zeros(7)
print(arr6)  #gives six zero

arr7=ones(9)
print(arr7)