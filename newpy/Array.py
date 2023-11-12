from array import *
vals=array('i',[2,3,56,7])
print(vals)
print(vals.buffer_info())
vals.reverse()#reverse the array
print(vals)

#
vals=array('i',[2,3,56,7])
# for i in range(4):
for i in range(len(vals)):#or for dynamic value
    print(vals[i])

#
# vals=array('i',[2,3,56,7])
# for e in vals:
#     print(e)

vals=array('i',[2,3,56,7])
new =array(vals.typecode,(a for a in vals))

# for e in new:
#      print(e)
# print()

#square of number in array
vals=array('i',[2,3,56,7])
new =array(vals.typecode,(a*a for a in vals))

for e in new:
     print(e)


#input array



