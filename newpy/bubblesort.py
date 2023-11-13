


def sort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j] > ls[j+1]:
               ls[j],ls[j+1] = ls[j+1],ls[j]
               print(ls)
            else:
               print(ls)


ls=[23,22,11,43,65,743,87,98,39]
sort(ls)