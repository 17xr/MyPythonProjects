from math import sqrt


def is_prime(num):
    # a variable to check primality of the number
    check = True
    # check is set to False is num is even or smaller than 2
    if num < 2 or (num % 2 == 0 and num > 2):
        check = False
    # check if num is divisible by any odd number from 3 to sqrt(num)
    for _ in range(3, int(sqrt(num))+1, 2):
        if num % _ == 0:
            check = False
    # print the result of the test
    if check:
        print("{} is a prime number !".format(num))
    else:
        print("{} is not a prime number !".format(num))
