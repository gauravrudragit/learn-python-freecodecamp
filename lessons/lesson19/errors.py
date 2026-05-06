class JustNotCoolError(Exception):
    pass


x = 2
try:
    # raise JustNotCoolError("This is not cool")
    # raise Exception("Custom exception")
    print(x/2)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("Do not divide by zero")
except Exception as error:
    print(error)
else:
    print("No errors")
finally:
    print("With or without errors")
