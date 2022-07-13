# Classic way by testing factors of the number
def is_prime(num):
    # a variable to check primality of the number
    check = True
    # check is set to False is num is even or smaller than 2
    if num < 2 or (num % 2 == 0 and num > 2):
        check = False
    # check if num is divisible by any odd number from 3 to sqrt(num)
    for _ in range(3, int(num ** 0.5) + 1, 2):
        if num % _ == 0:
            check = False
    # print the result of the test
    if check:
        print("{} is a prime number !".format(num))
    else:
        print("{} is not a prime number !".format(num))


# Another way of testing the primality of a number
def sieve_of_eratosthenes(num):
    # A list of boolean values set to True
    primes = [True for _ in range(num + 1)]
    # the number to start with (2 is the first prime number)
    i = 2
    # Run a while loop
    while i * i <= num:
        # if the number was prime
        if primes[i]:
            # since 'i' is a prime number, then all its factors are not
            for j in range(i * i, num + 1, i):
                primes[j] = False
        i += 1
    # Check if number is prime and print the result
    if primes[num]:
        print("{} is a prime number !".format(num))
    else:
        print("{} is not a prime number !".format(num))
        