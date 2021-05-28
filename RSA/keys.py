import sys
from algorithms import *


class RSA:
    def __init__(self, size):
        self.p = generate_prime(size)
        self.q = self.generate_q(size)
        self.r = rus_multiplication(self.p, self.q)
        self.euler = rus_multiplication(self.p - 1, self.q - 1)
        self.e = self.generate_e(size)
        self.d = self.generate_d()

    def generate_q(self, size):
        q = generate_prime(size)

        while q == self.p:
            q = generate_prime(size)
        return q

    def generate_e(self, size):
        while True:
            e = generate_prime(size)

            if e < self.euler:
                if co_prime(e, self.euler):
                    return e

    def generate_d(self):
        x, y, g = euclid(self.euler, self.e)

        if y <= 0:
            y += self.euler

        return y


class OpenPair:
    def __init__(self, e, r):
        self.e = e
        self.r = r


class ClosedPair:
    def __init__(self, d, r):
        self.d = d
        self.r = r
