import time
import random
import math
###
# Name: Slavic Heath
# Sorting Algorithms Implementation and Testing
###

#Problem1
def SelectionSort(Array):
    '''
    Take in a list and Perform Selection Sort
    :param Array: List of values
    :return: Sorted List
    '''
    n = len(Array)
    # Take a length of List and pick a value comparing all other values to it sorting list accordingly
    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if Array[j] < Array[minimum]:
                minimum = j
        Array[i], Array[minimum] = Array[minimum], Array[i]
    print("The selection list is", Array)


def BubbleSort(Array):
    '''
    Sort List Using Bubble Sort picking first value and comparing rest of the list to that value
    :param Array: List of Values
    :return: Sorted List
    '''
    n = len(Array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if Array[j + 1] < Array[j]:
                Array[j], Array[j + 1] = Array[j + 1], Array[j]
    print("The Bubblesort list is", Array)

#Problem2
def BruteForceStringMatch(Array, ArrayFind):
    n = len(Array)
    m = len(ArrayFind)
    counter = 0
    for i in range(0, n - m):
        j = 0
        counter += 1
        while j < m and ArrayFind[j] == Array[i + j]:
            counter += 1
            j = j + 1
        if j == m:
            return i
    print(counter)
    return -1

#Problem3
def BruteForceClosestPair(Array):
    distance = math.inf
    for i in range(0, len(Array)):
        for j in range(i + 1, len(Array)):
            x1 = Array[i][0]
            y1 = Array[i][1]
            x2 = Array[j][0]
            y2 = Array[j][1]
            euc = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
            distance = min(distance, euc)
    print("Closest 2 points distance is", distance)

def BruteForceClosestPairSqrt(Array):
    distance = math.inf
    for i in range(0, len(Array)):
        for j in range(i + 1, len(Array)):
            x1 = Array[i][0]
            y1 = Array[i][1]
            x2 = Array[j][0]
            y2 = Array[j][1]
            euc = (pow(x1 - x2, 2) + pow(y1 - y2, 2))
            distance = min(distance, euc)
    print("Closest 2 points distance is", math.sqrt(distance))


def main():
    # Problem 1
    print("Problem1")
    EmptyList = []
    EmptyList1 = []
    for i in range(0, 1000):
        n = random.randint(100, 3000)
        EmptyList.append(n)
        EmptyList1.append(n)
    start = time.perf_counter()
    SelectionSort(EmptyList)
    end = time.perf_counter()
    print("Time took to run Selection sort: ", end - start)

    start1 = time.perf_counter()
    BubbleSort(EmptyList1)
    end1 = time.perf_counter()
    print("Time took to run Bubble sort: ", end1 - start1)
    print("\n")

    # Problem 2
    print("Problem2 \n\n\n")
    EmptyList3 = []
    test1 = [0, 0, 0, 0, 1]
    number = 0
    while number < 1000:
        number += 1
        EmptyList3.append(0)
    print("The number of comperison is: ")
    BruteForceStringMatch(EmptyList3, test1)
    print("\n")

    # Problem 3
    print("Problem3 \n\n\n")
    for i in range(5, 1000,5):
        Array = []
        for n in range(100,3000):
            x1 = random.randint(1, 100000)
            y1 = random.randint(1, 100000)
            Array.append([x1, y1])
        print(Array)
        start = time.perf_counter()
        BruteForceClosestPair(Array)
        end = time.perf_counter()
        start1 = time.perf_counter()
        BruteForceClosestPairSqrt(Array)
        end1 = time.perf_counter()
        print("Time with square root: ", end - start)
        print("Time without the square root: ", end1 - start1)


main()
