def search(list,n):
    for i in range(0, len(list) , 1):
        if list[i] == n:
            # print('found')
            return True

        else:
            return False





list = [1,3,4,5,9]
n=1

if search(list,n):
    print('found')
else:
    print('not found')