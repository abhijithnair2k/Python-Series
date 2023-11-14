

# thousand seperaters
# def sep(num):
#     print(f"{num:,}")
# sep(30000)
# # palandrom
# # a ="hooh"
# a= input("enter the word").lower()
# ar = a.replace(" ","")
# if ar == ar[::-1]:   #to remove the space between the words
#     print("paladrom")
# else:
#     print("not palandrom")
# print(ar)
# print((a[0 : 3 : 2 ]))
# print((a[: : 2 ]))
# print((a[:  : -1]))
#######################
#Leap yera3###############
def leapyear(year):
    if year % 4 ==0 and (year % 100 !=0 or year % 400==0):

        print("its a leap year")
    else:
        print("its not a leap year")
year= int(input("enter the year"))

leapyear(year)


