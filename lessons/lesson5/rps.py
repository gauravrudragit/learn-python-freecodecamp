import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(1))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)


def validate_input(choice):
    return choice < 1 or choice > 3


print("")
player_choice = input("Enter...\n1:Rock\n2:Paper\n3:Sissors\n\n")
p_choice = int(player_choice)

if validate_input(p_choice):
    sys.exit("Incorrect input")

computer_choice = random.choice("123")
c_choice = int(computer_choice)

print("")
print("STAR GAME")
print("You chose:" + RPS(p_choice).name)
print("Python chose:" + RPS(c_choice).name)
print("")

if p_choice == c_choice:
    print("Draw")
elif p_choice == 1 and c_choice == 3:
    print("🎉 You win")
elif p_choice == 2 and c_choice == 1:
    print("🎉 You win")
elif p_choice == 3 and c_choice == 2:
    print("🎉 You win")
else:
    print("🐍 1Python wins")
