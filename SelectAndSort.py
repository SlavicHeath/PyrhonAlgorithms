# Problem 1
##################################
#Name: Slavic Heath

#####################################
import random
import time


def InsertionSort(Array):
    n = len(Array)
    compare = 0
    for i in range(1, n):
        v = Array[i]
        compare += 1
        j = i - 1
        while j >= 0 and Array[j] > v:
            Array[j + 1] = Array[j]
            compare += 1
            j = j - 1
        Array[j + 1] = v
    print("The number of comparisons: ", compare)
    return Array


# Problem 3
def RussianPeasant(n, m):
    product = 0
    div = 0
    mult = 0
    add = 0
    while n != 0:
        if n % 2 != 0:
            product = product + m
            add += 1
            m = m * 2
            mult += 1
            n = n // 2
            div += 1
        else:
            m = m * 2
            mult += 1
            n = n // 2
            div += 1

    total = add + mult + div  # total number of additions multiplications and divisions
    return product, total


# Problem 4
def LomutoPartition(Array, left, right):
    p = Array[right]
    s = left
    count = 0
    for i in range(left, right):
        count += 1
        if Array[i] <= p:
            Array[s], Array[i] = Array[i], Array[s]
            s += 1
    Array[s], Array[right] = Array[right], Array[s]
    count += 1
    print("The number of comparisons for Lomuto Partition is ", count)
    return s


def Quickselect(Array, left, right, k):
    s = LomutoPartition(Array, left, right)
    if s - left == k - 1:
        return Array[s]
    if s - left > k - 1:
        return Quickselect(Array, left, s - 1, k)
    return Quickselect(Array, s + 1, right, k - s + left - 1)


def main():
    # Problem 1
    A = [5, 3, 2, 7, 23, 43, 6, 9, 10]
    print(InsertionSort(A))
    # Problem 1
    print("Problem1")
    increase = 100
    for i in range(0, 8, 1):
        Array = []
        increase += increase
        for n in range(100, increase):
            x1 = random.randint(10, 3000)
            Array.append(x1)
        start = time.perf_counter()
        InsertionSort(Array)
        end = time.perf_counter()
        print("Time : ", end - start)

    # Problem 3
    x = 0
    y = 0
    for n in range(1, 21):
        x += 5000000
        y += 5000000
        print(x, y, RussianPeasant(x, y))

    # Problem 4
    newA = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    n = len(newA)
    print()
    print("The", 5, "th smallest value is:", Quickselect(newA, 0, n - 1, 5))


main()
