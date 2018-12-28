# cannibal_numbers.py - generates 2 random int, generates a list of int, and
# an (int, int) tuple. Evaluates based on the list and tuple

import random


def generate_list(i):
    '''(int) -> list of int

    Returns a list of an i number of int.
    '''

    return i, [random.randint(1, 25) for num in range(i)]

def generate_queries(j):
    '''(int) -> list of int

    Returns a list of a j number of int.
    '''

    return j, random.sample(range(35), j)

def evaluate_queries(num_list, queries_list):
    '''
    >>> evaluate_queries([3, 3, 3, 2, 2, 2, 1, 1, 1], [4, 5])
    [3, 3]
    >>> evaluate_queries([5, 4, 3, 2, 1], [4])
    [3]
    '''
    totals = []
    num_list.sort(reverse=True)
    
    for q in queries_list:
        remain_list = num_list.copy()
        total = 0
        for index in range(len(num_list)):
            num = num_list[index]
            if num >= q:
                total += 1
            elif len(remain_list) - 1 <= index or remain_list[-1] == num:
                break
            eaten = 0
            for needs in range(q - num):
                if len(remain_list) - 1 > index and num > remain_list[-1]:
                    remain_list.pop()
                    eaten += 1
                if eaten + num == q:
                    total += 1
                    
        totals.append(total)

    return totals

##import doctest
##doctest.testmod()
for i in range(5):
    i, num_list = generate_list(random.randint(1, 9))
    j, queries_list = generate_queries(random.randint(1, 9))
    totals = evaluate_queries(num_list, queries_list)
    print('Input: %s %s' % (i, j))
    print('Numbers: %s' % num_list)
    print('Queries: %s' % queries_list)
    print('Totals: %s' % totals)
    print()

