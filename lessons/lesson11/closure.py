# Closure is a function that has access to its parent functions scope after the parent function

def game(player, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 0:
            print(player + " has " + str(coins) + " coins left")
        elif coins <= 0:
            print(player + " has no coins left")

    return play_game


tom = game("tom", 5)
bob = game("bob", 10)

tom()
tom()
bob()
tom()
tom()
tom()
tom()
tom()
