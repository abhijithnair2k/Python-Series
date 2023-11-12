pos = -1
def search(list,n):
    i=0
    u=len(list)-1

    while i<=u:
        mid = (i+u) //2
        if(list[mid]==n):
            globals() ['pos']=mid
            return True
        else:
            if list[mid]<n:
                i=mid
            else:
                u=mid



list = [1,3,4,5,9]
n=3

if search(list,n):
    print('found at ', pos+1)
else:
    print('not found')