email = 'Abhijith@gmail.com'

print ("Your username : "+ email[ :email.index('@')])
print ("Your domain : " + email[ email.index('@')+1:])