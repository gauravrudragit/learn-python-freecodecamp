from functools import reduce
def squared(num): return num * num
# sq = lambda num : num * num


print(squared(2))


def s(a, b): return a + b
# s = lambda a,b : a + b


print(s(2, 2))

############################


def buildFn(x):
    return lambda num: num + x


addTen = buildFn(10)
add20 = buildFn(20)

print(addTen(5))
print(add20(2))

############################


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

############################


odd = filter(lambda num: num % 2 != 0, numbers)
print(list(odd))

############################

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

print(sum(numbers, 10))


names = ["Gaurav", "Dave", "John", "Bob"]
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
