##################################
#Name: Slavic Heath
#Unique Elements

#####################################

import random
import time

def UniqueElementsBruteForce(A):
    '''	       	   	  	
    This is an implementation of UniqueElements on page 63 in the Section 2.3.	       	   	  	
    :param A: A list of comparable elements	       	   	  	
    :return: True if all elements are unique; False, otherwise.	       	   	  	
    '''
    n = len(A)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return False
    return True

def InsertionSort(Array):
    # Inserion sort to sort for Presort
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

def PresortElementUniqueness(A):
    '''	       	   	  	
    This is an implementation of PresortElementUniqueness on page 203 Section 6.1.	       	   	  	
    :param A: A list of comparable elements.	       	   	  	
    :return: True if all elements are unique; False, otherwise.	       	   	  	
    '''
    n = len(A)
    for i in range(0, n - 1):
        if A[i] == A[i + 1]:
            return False
    return True

# The experiment

print("N\t\tBrute\t\t\t\t\t PreSort")
# your loop goes here that varies the size of n, perhaps from 100 up to 3000, stepsize 200



    # generate a list with "n" unique elements (e.g, 0, 1, 2, 3, 4, 5, 6 ...n-1)
n = 0
for i in range(0, 15):
    Array = []
    n += 200
    for j in range(100, n):
        x = random.randint(0, 1000)
        Array.append([x])


    # time the call to UniqueElementsBruteForce
    start = time.perf_counter()
    UniqueElementsBruteForce(Array)
    end = time.perf_counter()

    start2 = time.perf_counter()
    PresortElementUniqueness(Array)
    end2 = time.perf_counter()

    InsertionSort(Array)
    # time the call to PresortElementUniqueness
    start1 = time.perf_counter()
    PresortElementUniqueness(Array)
    end1 = time.perf_counter()

    # print n, a tab, the first timing, a tab, the second timing
    print("\n\n\n Presort List Sorted with QuickSort : ")
    print(len(Array), "\t", end-start, "\t", end1 - start1)

    print("\n\n\n Presort List not Sorted: ")
    print(len(Array), "\t", end - start, "\t", end2 - start2)