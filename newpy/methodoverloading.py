class Student:
    def __init__(self , s1,s2):
        self.s1 = s1
        self.s2 = s2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a + b+ c
        elif b!=None and a!=None:
            s=a + b
        else :
            s = a
        return s


        return s
s1=Student(23,32)
print(s1.sum(2))



