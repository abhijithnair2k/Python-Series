# prime number
r=12
for num in range(2,r):
    if r%num==0:
        print("not prime")
        break
else:
        print("prime")
