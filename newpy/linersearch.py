

pos=0
def search(li,n):
    i = 0
    while i < len(li):
        if li[i] == n :
            globals() ['pos'] = i
            return True
        i = i + 1

    return False









li = [2,1,4,76,54,34]
n = int(input("enter the number"))
if search(li,n):
    print("found at", pos )
else:
    print("not found")