from array import *
# arr=array('i',[])
#
# t=int(input("enter the range"))
# for i in range(t):
#     x=int(input("enter the value"))
#     arr.append(x)
# print(arr)

arr=array('i',[1,2,3,4,5])
val=int(input("enter the value to search"))
k=0
for e in arr:
 if e==val:
     print(k)
     break
 k=k+1

print(arr.index(val)) #to find the index of these