from algorithms import *


class Hash:
    def __init__(self, message, p, q):
        self.message = message
        self.n = rus_multiplication(p, q)
        self.h = self.hash_function()

    def hash_function(self, h=12345):
        for char in self.message:
            h = mod_exp(h, ord(char), self.n)

        return h


class HashPair:
    def __init__(self, size):
        self.p = generate_prime(size)
        self.q = generate_prime(size)
        self.is_equal(size)

    def is_equal(self, size):
        while self.p == self.q:
            self.q = generate_prime(size)
