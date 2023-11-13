name= ( "Abhijith","Ebin","Ajith")
place= ("Malyadi","kovilpallayam","kovilpatti")
zipping= list(zip(name,place))
zipping1= set(zip(name,place))
zipping2= dict(zip(name,place))
for (a,b) in zipping:
    print(a,b)
print(zipping1)
print(zipping2)