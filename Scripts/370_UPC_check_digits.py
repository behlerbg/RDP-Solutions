#! python3
## 370_UPC_check_digits.py
## Defines a function that provides the final digit in a valid UPC-A code.
## Brett Behler 12.28.2018

def upc_check(upc):
    '''(str) || (int) --> (int)

    Given a <= 12 digit upc, return the final check digit that would make a
    valid UPC-A code. Returns -1 if given upc is has 12 or more digits or
    contains a non-numeral.

    >>> upc_check(4210000526)
    4
    >>> upc_check(3600029145)
    2
    >>> upc_check(12345678910)
    4
    >>> upc_check(1234567)
    0
    >>> upc_check(123456789012)
    -1
    >>> upc_check(12A456)
    -1
    >>> upc_check(1234567890123)
    -1

    '''
    checksum = 0 
    num_list = [num for num in '{upc:0>11}'.format(upc=str(upc))]
    if len(num_list) >= 12:
        return -1
    for i in range(len(num_list)):
        try:
            if i % 2 == 0:
                checksum += int(num_list[i]) * 3
            else:
                checksum += int(num_list[i])
        except ValueError:
            return -1
    if checksum % 10 == 0:
        return 0
    else:
        return (10 - (checksum % 10))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
