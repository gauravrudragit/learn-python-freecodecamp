def hello():
    print("Hello !!")


hello()


def sum(num1, num2=3):
    if (isinstance(num1, int) and isinstance(num2, int)):
        return num1+num2
    else:
        print("Incorrect Input")


print(sum('A', 2))
print(sum(1, 2))
print(sum(1))


def mulitple_args(*args):
    print(args)
    print(type(args))
    print(len(args))


mulitple_args(1, 2, 3, 'a')


def multi_name_args(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_name_args(first="a", last="b")
