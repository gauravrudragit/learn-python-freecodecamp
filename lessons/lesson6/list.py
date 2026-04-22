users = ['Dave', 'John']

data = ['Dave', 42]

empty_list = []

print("Dave" in empty_list)
print(users[0])
print(users[-1])

print(users.index('Dave'))
print(users[0:1])
print(users[0:])

print(len(users))
users.append("Gaurav")

print(users)

users += ['Rudra', 'Praj']
print(users)

users.extend(['A', 'B'])
print(users)

users.extend(data)
print(users)

users.insert(0, 'Bob')
print(users)

users[1:1] = ['X', 'Y']
print(users)

users[1:3] = ['X', 'Y']
print(users)

users.remove('Bob')
print(users)

users.pop()
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[0:0] = ['abc']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynum = list(nums)
mycopy = nums[:]

print(type(nums))

list1 = list('gaurav')
print(list1)

list2 = list(['gaurav'])
print(list2)

# Tuples(A list that does not change)

atuple = tuple(('a', 'a', 'b'))
print(atuple)

newtuple = (1, 2, 2, 4)  # Packing a tuple
(one, *two, rest) = newtuple  # Unpacking a tuple

print(one)
print(two)
print(rest)

print(atuple.count(1))
