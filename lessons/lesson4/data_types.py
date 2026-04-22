# String data type

# literal assignment
import math
first = 'Gaurav'
last = 'Rudra'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor fn
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Conactenation
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Cast to string
# decade = str(1980)
# print(type(decade))
# print(decade)

# Mulitple lines
statement = '''
Hey
How are you?
                Just checking in. All good     


'''

# print(statement)

# Escape char
# sentence = 'I\'m back at work!\tHey!\nHow are you\\'
# print(sentence)

# String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(statement.title())
# print(statement.replace("good", "ok"))

# print(len(statement))
# statement += "           "
# statement = "           " + statement
# print(len(statement))

# print(len(statement.strip()))
# print(len(statement.lstrip()))
# print(len(statement.rstrip()))
# print('        ')

# # Build menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cake".ljust(16, ".") + "$3".rjust(4))

# string index
# print(first[0])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])
# print(first[1::2])

# # Float
# gpa = 3.14
# print(abs(gpa * -1))
# print(round(gpa))
# print(round(gpa, 1))

print(math.pi)

zipcode = "10001"
zip_v = int(zipcode)
print(type(zip_v))

zip_val = int("New")
