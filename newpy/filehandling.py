o= open("Myprofile",'w')
print(o)
l= open("Myprofile",'a')
print(l.write("Hai i love you"))

q= open("Myprofile",'r')
print(q.read())
print(q.readline(),end="")
print(q.readline())


for data in q:
    o.write(data)

