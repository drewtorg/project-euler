from math import sqrt

def sieve_of_eratosthenes(n):
	sieve = range(n)
	sieve[1] = 0
	for x in xrange(2, int(sqrt(n))):
		if sieve[x] > 0:
			for q in xrange(x*x, n, x):
				sieve[q] = 0
	return sum(sieve)
	
print sieve_of_eratosthenes(2000000)