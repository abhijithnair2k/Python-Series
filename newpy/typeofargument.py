#formal Argument and  Actual argument
def person (name,age):
    print(name)
    print(age)
    # print(c)
person('abhi',23)

def person (name,age):
    print(name)
    print(age)
    # print(c)
person(name='abhi',age=23)

#variable Length##
# if we add more than a value to a varaiable it wuill cause varable length
def add(a,*b):
    d=a
    for i in b:
      d=d+i

    print(d)

add(5,6,7,8)

# key length variable

# global variable

a=10
def detailssum ():
    a=17
    b=globals()['a']
    print(a+b)
    globals()['a']=15
detailssum()

