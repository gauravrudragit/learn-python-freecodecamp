person = "gaurav"
coins = 2

# Older ways

print("\n" + person + " has " + str(coins) + " coins")
print("\n{} has {} coins".format(person, coins))
print("\n{1} has {0} coins".format(coins, person))
print("\n{p} has {c} coins".format(c=coins, p=person))

player = {
    "person": "Gaurav",
    "coins": 2
}

message = "\n{person} has {coins} coins".format(**player)
print(message)

# New way f-strings

message = f"\n{person} has {coins} coins"
print(message)
message = f"\n{person} has {2 * 10} coins"
print(message)
message = f"\n{person.upper()} has {coins} coins"
print(message)
message = f"\n{player['person']} has {coins} coins"
print(message)

num = 10
print(f"\n{num} squared is {num ** 2:.4f}")  # f -> fixed

print(f"\n{num} divided by 2 is {num/2:%}")
