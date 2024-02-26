import math
import random
import time


def HoarePartition(Array, l, r):
    medianleft = Array[l]
    medianright = Array[r]
    p = (medianleft + medianright) // 2
    i = l - 1
    j = r + 1

    while True:
        i += 1
        while Array[i] < p:
            i += 1
        j -= 1
        while Array[j] > p:
            j -= 1
        if i >= j:
            return j
        Array[i], Array[j] = Array[j], Array[i]


def quicksort(a, low, high):
    if low < high:
        pivot = HoarePartition(a, low, high)

        quicksort(a, low, pivot)

        quicksort(a, pivot + 1, high)


def merge(Array, A, B):
    i = 0
    j = 0
    k = 0
    p = len(A)
    q = len(B)
    while i < p and j < q:
        if A[i] <= B[j]:
            Array[k] = A[i]
            i += 1
        else:
            Array[k] = B[j]
            j += 1
        k += 1
    while i < p:
        Array[k] = A[i]
        i += 1
        k += 1
    while j < q:
        Array[k] = B[j]
        j += 1
        k += 1
    return Array


def mergeSort(Array):
    if len(Array) > 1:
        a = len(Array) // 2
        l = Array[:a]
        r = Array[a:]
        mergeSort(l)
        mergeSort(r)
        return merge(Array, l, r)


def main():
    A = [2, 3, 41, 243, 23, 1, 6]
    n = len(A)
    quicksort(A, 0, n - 1)
    for i in range(n):
        print(A[i], end=" ")
    A1 = [2, 3, 41, 243, 23, 1, 6, 82, 4]
    print("\n")
    print(mergeSort(A1))
    print("\n")
    print("Quicksort")
    increase = 0
    for i in range(0, 20):
        Array1 = []
        n1 = len(Array1)
        increase += 50000
        for n in range(0, increase):
            x = random.randint(10, 30000)
            Array1.append(x)
        start = time.perf_counter()
        quicksort(Array1, 0, n1 - 1)
        end = time.perf_counter()
        print(len(Array1), "\t", end - start)

    print("Merge")
    increase1 = 0
    for i in range(0, 20):
        Array2 = []
        increase1 += 50000
        for n in range(0, increase1):
            x1 = random.randint(10, 30000)
            Array2.append(x1)
        start1 = time.perf_counter()
        mergeSort(Array2)
        end1 = time.perf_counter()
        print(len(Array2), "\t", end1 - start1)

    print("Quicksort with 2 Sorted Arrays combined")
    increase = 0
    for i in range(0, 100, 10):
        Array = []
        Array1 = []
        increase += 100
        for i in range(0, increase):
            x = random.randint(0, 10000)
            x1 = random.randint(0, 10000)
            Array.append(x)
            Array1.append(x1)
        #print("Before Sort")
        #print(Array)
        Array.sort()
        #print("After Sort")
        #print(Array)
        #print("Before Sort 1")
        #print(Array1)
        Array1.sort()
        #print("After Sort 1")
        #print(Array1)
        #print("Combined List")
        Array.extend(Array1)
        #print(Array)
        n = len(Array)
        start = time.perf_counter()
        quicksort(Array, 0, n - 1)
        end = time.perf_counter()
        print(n, "\t", end - start)
        # for i in range(n):
        #     print(Array[i], end=" ")
    print("Merge Sort with 2 Sorted Arrays combined")
    increase = 0
    for i in range(0, 100, 10):
        Array = []
        Array1 = []
        increase += 100
        for i in range(0, increase):
            x = random.randint(0, 10000)
            x1 = random.randint(0, 10000)
            Array.append(x)
            Array1.append(x1)
        # print("Before Sort")
        # print(Array)
        Array.sort()
        # print("After Sort")
        # print(Array)
        # print("Before Sort 1")
        # print(Array1)
        Array1.sort()
        # print("After Sort 1")
        # print(Array1)
        # print("Combined List")
        Array.extend(Array1)
        # print(Array)
        n = len(Array)
        start = time.perf_counter()
        mergeSort(Array)
        end = time.perf_counter()
        print(n, "\t", end - start)
main()
