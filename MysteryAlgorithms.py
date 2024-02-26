##################################
#Name: Slavic Heath
#Exercises on evaluating algorithms and what they do

#####################################
import random
import time

#Problem 1 Computes the sum of squares of number 1 to n
def Mystery(n):
    S = 0 # set sum to 0
    for i in range(1,n): #numbers between 1 and n
        S = S + i * i #square with each occurence and ad to the sum
    return S

#Problem 2 Checks any matices and if they are symetric
def Enigma(A,m):
    for i in range(0, m-2):
        for j in range(i+1, m-1):
            if (A[i][j] != A[j][i]):
                return False
    return True


#Probelm 3 Squares a function
def Q(n):
    if n == 1:
        return 1
    else:
        return Q(n-1) + 2 * n + 1

#Problam 4 Gives the smallest value in the array
def Riddle(A, n):
    if n == 1:
        return A[0]
    else:
        temp = Riddle(A,n-1)
        if temp <= A[n-1]:
            return temp
        else:
            return A[n-1]

def main():

    #Problem 1 Test
    for n in range(10, 1500, 100):
        start = time.perf_counter()
        test = Mystery(n)
        endTime = time.perf_counter()
        print(n, "\t", endTime - start)

    print("\n")
    A = [[7, 9, 4],[3,4,5]]
    #Problem 2 Test
    res = [[5, 1, 3], [2, 0, 2], [3, 1, 5]]
    print(Enigma(res, 3))

    print("\t")
    #Problem 3 Test

    for n in range(10, 100, 10):
        start = time.perf_counter()
        test = Q(n)
        endTime = time.perf_counter()
        print(n, "\t", endTime - start)

    n = random.randint(0, 10)
    print(Q(n))

    print("\t")
    #Problem 4 Test

    A = [4,8,5,6,7,3,43,23,54,32]
    print(Riddle(A,3))



main()