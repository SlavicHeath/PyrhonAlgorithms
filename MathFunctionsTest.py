from testing import *
from MathFunctions import *


def main():
    a = [9, 4, 2, 3, 5, 9, 10]
    c = [9, 4, 2, 3, 5, 9, 11]
    b = [3, 4, -1, 9, 99, 12, 34]

    test(sum(a) / len(a), average, a)

    test([9 / 1, 13 / 2, 15 / 3, 18 / 4, 23 / 5, 32 / 6, 42 / 7], moving_average, a)

    test([3 / 1, 7 / 2, 6 / 3, 15 / 4, 114 / 5, 126 / 6, 160 / 7], moving_average, b)

    test(False, is_unique, a)

    test(False, is_unique, c)

    test(True, is_unique, b)

    test([10, 11], diff, a, c)

    test([-1, 2, 5, 10, 12, 34, 99], diff, a, b)

    test(2, kth_smallest, [3, 2, 12, 11, 5, 2, 3, 11, 10, 22, 12, 12, 5, 6], 1)
    test(4, kth_smallest, [4, 1, 2, 12, 11, 5, 2, 4, 11, 34, 22, 22, 34, 10, 22, 1, 1, 1, 5, 6], 3)
    test(6, kth_smallest, [2, 1, 2, 12, 11, 5, 2, 4, 11, 34, 22, 22, 34, 10, 62, 1, 1, 1, 5, 6], 5)
    test(10, kth_smallest, [1, 1, 2, 12, 11, 5, 2, 4, 11, 36, 22, 22, 36, 10, 42, 1, 1, 1, 5, 6], 6)


main()
