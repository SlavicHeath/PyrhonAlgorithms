import random

#return a list of length size filled with random ints in the range low-->high, both inclusive
def random_list(size, low, high):
    random.seed()
    a = [random.randint(low, high) for r in range(size)]
    return a
