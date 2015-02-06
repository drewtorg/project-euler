import random
from math import log

def is_fermat_prime(n, ntrials):
    random.seed()
    for x in range(0, ntrials):
        rand = random.randint(1, n - 1)
        if (rand ** n) % n != rand:
            return False
    return True

def find_nth_fermat_prime(nth, ntrials):
    i = 3
    n = 2
    while n < nth:
        i += 2
        if is_fermat_prime(i, ntrials):
            n += 1
    return i

print find_nth_fermat_prime(1000, 10)

