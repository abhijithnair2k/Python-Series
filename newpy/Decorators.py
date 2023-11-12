def div(a,b):
 print(a/b)


def smort_div(func):
     def inner(a,b):
         if a<b :
             a,b = b,a
         return func(a,b)
     return inner()
div = smort_div(div)
div(3,6)