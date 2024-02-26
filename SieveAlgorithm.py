import math
import random
import time

def sieve(num):
    prime = []
    for i in range(2, num + 1):
        prime.append(i)
    print("List before: ", prime)
    i = 2
    while (i <= int(math.sqrt(num))):
        if i in prime:
            # If Duplicates Found Remove from list
            for j in range(i * 2, num + 1, i):
                if j in prime:
                    prime.remove(j)
        i = i + 1
    return print("List of all primes: ", prime)


def main():
    n = 25
    sieve(n)

main()