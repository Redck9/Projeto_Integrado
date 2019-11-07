import random


def private_key(p):
    return random.randint(2, p - 1)


def public_key(p, g, private):
    return (g ** private) % p


def secret(p, public, private):
    return modular_exponentiation(public, private, p)


def modular_exponentiation(public, private, prime):
    res = 1
    public %= prime
    while private > 0:
        if private & 1:  # if private is odd
            res = (res * public) % prime  # take a power off
        private = private >> 1      # private = private/2
        public = (public * public) % prime

    return res