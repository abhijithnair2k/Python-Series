


pos = 0
def search(list,n):
    lower = 0
    higher = len(list)-1
    while lower <= higher:
        mid = (lower+higher)//2
        if list[mid] == n:
            globals()['pos' ]= mid
            return True
        else:
            if list[mid] < n:
                lower = mid +1
            else:
                higher = mid -1





list = [2,1,34,54,3,56,32,98,100]
list.sort()
print(list)
n=98
if search(list,n):
    print("found" , pos)
else:
    print("not found")