from numpy import *
#vectirozed operation
axx1 = array([9, 8, 7, 6, 5])
axx2 = array([1, 2, 3, 4])

# att3 = axx1 + axx2
# print(att3)
print(cos(axx2))

print(sin(axx2))

print(min(axx2))

print(max(axx2))
print(concatenate([axx2,axx1]))


####################
# coping array

axx1 = array([9, 8, 7, 6, 5])
axx1[1]=6

axx3=axx1
print(axx3)##shadow coping with same array and provides same reference but the change in one array will cj=hange the other array
print(axx1)
print(id(axx1))
print(id(axx3))
## to change the address
axx1 = array([9, 8, 7, 6, 5])
axx1[1]=6

axx3=axx1.view()
print(axx3)
print(axx1)
print(id(axx1))
print(id(axx3))
#####
# DeepCopy


axx1 = array([9, 8, 7, 6, 5])
axx3=axx1.copy()
axx1[1]=66

print(axx3)
print(axx1)
print(id(axx1))
print(id(axx3))