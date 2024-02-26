##################################
#Name: Slavic Heath
#Euclids methods calculating GCD

#####################################

import time
import random

def iterate(m, n):
    '''
    Iterative method for finding GCD
    :param m: value 1
    :param n: value 2
    :return: GCD Value
    '''
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


def recurse(m, n):
    '''
    Recursive method for fidning GCD
    :param m: value 1
    :param n: value 2
    :return: GCD Value
    '''
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        return recurse(n, m % n)


def consecutive(m, n):
    '''
       Consecutive method for fidning GCD
       :param m: value 1
       :param n: value 2
       :return: GCD Value
    '''
    t = min(m, n)
    while t != 0:
        if m % t == 0:
            if n % t == 0:
                return t
            t = t - 1
        else:
            t = t - 1
    return m



def main():
    '''
    Test each function with different values large and small values
    :return: time takes to complete each algorithm in seconds
    '''
    a = 60
    b = 24

    print("Iterative")
    starting = time.perf_counter()
    con = iterate(a, b)
    end = time.perf_counter()
    print("Time took to compute GCD of", a, "and", b, float("%.20f" % (end - starting)), "Result: ", con)

    print("Recursively")
    starting = time.perf_counter()
    con = recurse(a, b)
    end = time.perf_counter()
    print("Time took to compute GCD of", a, "and", b, float("%.20f" % (end - starting)), "Result: ", con)

    print("Consecutively")
    starting = time.perf_counter()
    con = consecutive(a, b)
    end = time.perf_counter()
    print("Time took to compute GCD of", a, "and", b, float("%.20f" % (end - starting)), "Result: ", con)

    print()
    print()
    print()

    #Large number test 500 - 1000
    list = []
    for i in range(0,3):
        m = random.randrange(500, 1000)
        n = random.randrange(500, 1000)
        print("Iterative")
        starting = time.perf_counter()
        con = iterate(m, n)
        end = time.perf_counter()
        timeresult = end - starting
        print("Time took to compute GCD of", m, "and", n, float("%.20f" % (timeresult)), "Result: ", con)
        list.append(float("%.20f" % (timeresult)))
    print(list)
    print()
    print()
    print()

    list1 = []
    for i in range(0, 3):
        m = random.randrange(500, 1000)
        n = random.randrange(500, 1000)
        print("Recursive")
        starting = time.perf_counter()
        con = recurse(m, n)
        end = time.perf_counter()
        timeresult = end - starting
        print("Time took to compute GCD of", m, "and", n, float("%.20f" % (timeresult)), "Result: ", con)
        list1.append(float("%.20f" % (timeresult)))
    print(list1)

    print()
    print()
    print()

    list2 = []
    for i in range(0, 3):
        m = random.randrange(500, 1000)
        n = random.randrange(500, 1000)
        print("Consecutively")
        starting = time.perf_counter()
        con = recurse(m, n)
        end = time.perf_counter()
        timeresult = end - starting
        print("Time took to compute GCD of", m, "and", n, float("%.20f" % (timeresult)), "Result: ", con)
        list2.append(float("%.20f" % (timeresult)))
    print(list2)

main()
