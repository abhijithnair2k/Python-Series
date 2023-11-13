a = 10
b = 0


try:
    e= a/b

except Exception as e:

    print("its a invalid input",e)
finally:
    print("finally print this")