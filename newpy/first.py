from builtins import print, len

from unicodedata import name

print(8//4 )

print(2**3)
print(90**3)
print('navin')
print("navins's laptop")
print('navin\'s "laptop" ' )
print(20*'Abhi')
# to raw String
print(r'navins\n laptop ')
x=2
print(x)
print(3+x)
name='Abhijith'
print(name)
print(name[2])
print(name[-2])
print(name[0:5])
print(len(name))
#  List

digits=[10,11,12,13,14]
print(digits[2])
print(digits[2:9])
name=["Murali","Ajith","Ebib"]
print(name[2])
age=[21,22,23]
mil=[name,age]
print(mil)
age.append(20)
print(age) #add at the end
age.sort()  #sorting in ascending order
print(age)
age.insert(2,88)
print(age)
age.remove(88)
print(age)
age.pop(2) #used to delete a element  according to the index value
print(age)
age.pop() #if not with index it will delete the last value
print(age)
age.extend([22,23,25,26])
print(age)
min(age)
print(min(age))
################################
#Tuple

value=(19,20,30,40)
print(value.count(40))
# print(value.index([19,20])#
#################################################
#Set

abhi={60,65,89,9}
print(abhi)###sequeence is not maintained
abhi.add(200)
print(abhi)

#########################################
#Dictnory

name={ 1:'ebin', 2:'shalu',3:'sujin',4:'vava'}
print(name[1])

names=['ajay','sajin','ajith']
age=[22,23,24]
details=dict(zip(names ,age))
print(details)
details['monika']=27#to add aelement
print(details)
del details['ajay']#TO DELETE A ELEMENT
print(details)

rom={ 'java':'abhi','python':'ajith','css':['athira','najjeb'],'html':{'najjeb':'chechi','najeeb':'thata'}}
print(rom)
print(rom['css'])
print(rom['html']['najjeb'])





#########################################################






