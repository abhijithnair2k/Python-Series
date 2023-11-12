from numpy import *
arr1=array([
    [1,2,3,0,7,6],
    [4,5,6,3,4,5]
])
print(arr1)
print(arr1.dtype)
print(arr1.shape)
print(arr1.ndim)# provide the dimension of array
arr2=arr1.flatten()
print(arr2)
print(arr2.reshape(4,3))#reshape the array

#################


# matrix

m=matrix(arr1)
print(m)

m1=matrix('1,2,3;4,5,6;8,9,10')
print(m1)
print(diagonal(m1))#diagonaL ELEMENTA

print(m1.max())
print(m1.shape)

m1=matrix('1,2,3;4,5,6;8,9,10')
m2=matrix('1,2,3;4,5,6;8,9,10')
m3=m1*m2
print(m3)#multiplicationare done in this matrix
#addidtion can also be possible  And anothe operation

