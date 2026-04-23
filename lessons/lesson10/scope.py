name = "Gaurav"
count = 1


def greet(name):
    global count
    print(count)
    print("Hello " + name)
    count += 2
    print(count)
    color = "blue"

    def another(name):
        nonlocal color
        color = "red"
        print(color)

    print(color)
    another(name)


greet("gaurav")
