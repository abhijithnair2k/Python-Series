def square():
    n = 1
    while n<=10:
       sq=n*n
       yield sq
       n= n + 1
value = square()
for i in value:
 print(i)
def ass():
    yield 5
p=ass()
print(next(p))