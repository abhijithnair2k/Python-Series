from numpy import *
def add(x,y):
    s=x+y
    print(s)

add(1,2)

def add(x,y):
    s=x-y
    return s

result=add(9,2)
print(result)

def add_sub(x,y):
    s=x-y
    y=x+y
    return s,y

result=add_sub(9,2)
print(result)
#################### #modularity