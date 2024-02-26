# Complete the functions below as directed in the assignment
# Document each function using docstring comments
# test the functions by running MathFunctionsTest.py
def average(a_list):
    '''
    Find Average of all values in a list
    :param a_list: list of values
    :return: Average of all values
    '''
    sum = 0  # sum to for all values
    for num in range(0, len(a_list)):  # iterate through values and divide sum by the length of the list
        sum += a_list[num]
        average = sum / len(a_list)
    return average


def moving_average(a_list):
    '''
    Take a list and iterate adding values and giving the average values of adding next values in the list
    :param a_list: list of values
    :return: list of moving averages of the same size as a given list
    '''
    # empty list
    avg_list = []
    total = 0  # total of the list

    # loop to find the moving_averages
    for num in range(len(a_list)):
        total += a_list[num]  # total of the first values added

        avg_list.append(total / (num + 1))  # dvide total by the next added value

    return avg_list


def is_unique(a_list):
    '''
    Check a_list for Duplicates if Found duplicate return False else True
    :param a_list: list to be iterated
    :return: Boolean True or False
    '''
    for num in range(0, len(a_list)):  # iterate starting with first value
        for nextNum in range(num + 1, len(a_list)):  # Iterate starting with second value
            if a_list[num] == a_list[nextNum]:  # Compare the values and return answer
                return False
    return True


def diff(a_list, b_list):
    '''
    Take two lists and compare finding values that are not present in both lists
    :param a_list: first list
    :param b_list: second list
    :return: List with ddifferent values
    '''
    c_list = []  # list holding numbers from 2 lists
    # loop to find unique values in a_list
    for i in range(len(a_list)):
        flag = 1
        for j in range(len(b_list)):  # check in b_list
            if a_list[i] == b_list[j]:  # if found break
                flag = 0
                break
        if flag == 1:  # flag is still 1 means no duplicate found in b
            c_list.append(a_list[i])  # append the number to c_list
    # same as above but to find unique values of b_list
    for i in range(len(b_list)):
        flag = 1
        for j in range(len(a_list)):  # check in a_list
            if b_list[i] == a_list[j]:
                flag = 0
                break
        if flag == 1:  # if unique append the number to c_list
            c_list.append(b_list[i])
    return c_list


def kth_smallest(a_list, k):
    '''
    Check a_list and give the smallest value in the list ignoring duplicates
    :param a_list: list to be sorted and iterated
    :param k: smallest spesified value in a list
    :return: the smallest value of k
    '''
    # sort the list
    a_list.sort()

    # set unique_count to 0
    unique_count = 0

    # loop to check the kth number and return it.
    for num in range(len(a_list) - 1):  # iterate through the back of the list

        if a_list[num] != a_list[num + 1]:  # check for unique values and increase unique count
            unique_count += 1

        if unique_count == k:  # Confirm that the count is the same as value needed to displayed without duplicates
            return a_list[num]  # return value of a list when unique_count value matches the k value
