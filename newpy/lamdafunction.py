f= lambda a,b : a+b
result= f(10,20)
print(result)

##################map()############

num=[2,4,6,45,67,86,98]
evens=list(filter(lambda n : n%2==0,num) )
double=list(map(lambda n : n*2,evens))
print(double)
print(evens)

