import math
import copy
import random
import time

###
# Take 2 Points on x,y axes and find the closest distance between them by brute force
# Name: Slavic Heath
###


class Point():
    '''
    Create point class that takes x and y values
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

def brute_force(P, n):
    '''
    Create a class that creates and takes multiple points and finds a minimum distance between them
    :param P: Point (x,y)
    :param n: number of points
    :return: the minimum distance between 2 points
    This algorithm is inefficient and tend to be slow in addition not as constructive
    '''
    minimum = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            # Minimum distance function
            distance = math.sqrt((P[i].x - P[j].x) ** 2 + (P[i].y - P[j].y) ** 2)
            if distance < minimum:
                minimum = distance
    return minimum

def EfficientClosestPair(P, Q, n):
    '''
    Efficiency algorithm for finding minimum distance between Points
    :param P:  point on x,y axes
    :param Q: point to compare to
    :param n: number of points
    :return: minimum distance between pairs of points
    '''
    global min1
    # If there are less than 3 points compute brute force
    if n <= 3:
        return brute_force(P, n)

    # Split list of points in 2 and find the midpoint
    mid = n // 2
    midpoint = P[mid]

    # Split into left half and right half
    Pleft = P[:mid]
    Pright = P[mid:]

    # Recursively divide list into smaller half's
    kleft = EfficientClosestPair(Pleft, Q, mid)
    kright = EfficientClosestPair(Pright, Q, n - mid)

    k = min(kleft, kright)

    # Create new list of points and closest points
    P = []
    Closest = []
    lr = Pleft + Pright
    # Functions funding and adding to the list for Closest distance between points
    for i in range(n):
        if abs(lr[i].x - midpoint.x) < k:
            P.append(lr[i])
        if abs(Q[i].x - midpoint.x) < k:
            Closest.append(Q[i])
# list, size, k
    P.sort(key=lambda point: point.y)
    # Sort the list and find the clossest distance
    for i in range(len(P)):
        j = i + 1
        while j < len(P) and (P[j].y -P[i].y) < k:
            k = math.sqrt((P[i].x - P[j].x) ** 2 + (P[i].y - P[j].y) ** 2)
            j += 1
        min1 = k
        while j < len(Closest) and (Closest[j].y - Closest[i].y) < k:
            k = math.sqrt((Closest[i].x - Closest[j].x) ** 2 + (Closest[i].y - Closest[j].y) ** 2)
            j += 1
        min2 = k
    return min(min1, min2)

def main():
    '''
    Test Function to test time efficiency between brute force algorithm and efficiency algorithm
    '''
    # Create a list of random points and find distance timing both functions 10 times
    increase = 10
    for i in range(0,100, 10):
        increase +=10
        P = []
        for j in range(0, increase):
            i= Point(random.randint(0,1000), random.randint(0,1000))
            P.append(i)
        n = len(P)
        P.sort(key=lambda point: point.x)
        Q = copy.copy(P)
        Q.sort(key=lambda point: point.y)

        # Time Efficiency
        start = time.perf_counter()
        EfficientClosestPair(P, Q,n)
        end = time.perf_counter()

        # Time Brute Force
        start1 = time.perf_counter()
        brute_force(P,n)
        end1 = time.perf_counter()
        print(n, "\t", end - start, "\t", end1 - start1)


main()