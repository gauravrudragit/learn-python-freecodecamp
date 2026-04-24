from random import choice


def random_fact():
    facts = ("Hi this is fact 1", "Hi this is fact 2", "Hi this is fact 3")
    index = choice("012")
    return facts[int(index)]


# This code will only run if this file is run directly, not when imported as a module
if __name__ == "__main__":
    print(random_fact())
