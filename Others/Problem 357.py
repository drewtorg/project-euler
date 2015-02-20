from math import sqrt
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def generate_sieve(limit):
	ubound = limit + 1

	size = (ubound - 3) / 2
	a = [False] * size
	s = 0
	primes = [1,2]
	while s < size:
	    t = 2 * s
	    p = t + 3
	    primes.append(p)
	    for n in range(t * (s + 3) + 3, size, p):
	        a[n] = True
	    s = s + 1
	    while s < size and a[s]:
	        s = s + 1
	return primes

def is_prime_generator(n,sieve):

	for d in xrange(1,int(sqrt(n)) + 1):
		#if we have a divisor, check to see it is prime
		if n % d == 0:
			if not is_prime(d + (n / d), sieve):
				return False
	return True

def is_prime(n,sieve):
	if binary_search(sieve, n) == -1:
		return False
	return True

def main(n,sieve):
	f = open('output.txt', 'w')
	Sum = 0
	for i in xrange(1,n):
		if is_prime_generator(i, sieve):
			f.write(str(i)+'\n')
			Sum += i
	print Sum

limit = 100000000
sieve = generate_sieve(limit+2)
main(limit,sieve)

#runs in 404.9s