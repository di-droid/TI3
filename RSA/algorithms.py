import random
import math


def euclid(a, b):
    if not b:
        return 1, 0, a
    y, x, g = euclid(b, a % b)
    return x, y - (a // b) * x, g


def co_prime(a, b):
    return math.gcd(a, b) == 1


def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)


def fast_pow(number, power):
    if power == 0:
        return 1
    elif power == -1:
        return 1. / number

    p = fast_pow(number, power // 2)
    p *= p

    if power % 2:
        p *= number

    return p


def rus_multiplication(first_num, second_num):
    temp = 0
    while second_num > 0:
        if second_num % 2 == 1:
            temp = temp + first_num

        first_num = first_num << 1
        second_num = second_num >> 1
    return temp


def eratosthenes_sieve(n):
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

    return tuple(lst)


def is_prime_test(number, num_of_tests=5):
    s = 0
    d = number - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert(fast_pow(2, s) * d == number - 1)

    def trial_composite(a):
        if pow(a, d, number) == 1:
            return False
        for ind in range(s):
            if pow(a, fast_pow(2, ind) * d, number) == number - 1:
                return False
        return True

    for i in range(num_of_tests):
        num = random.randrange(2, number)
        if trial_composite(num):
            return False

    return True


def generate_prime(size):
    max_prime = fast_pow(2, size) / 2
    sieve = eratosthenes_sieve(1000)

    while True:
        prime = random.randint(2, max_prime)

        if prime % 2 == 0:
            continue

        for i in sieve:
            if prime % i == 0:
                continue

        if is_prime_test(prime, 3):
            return prime
