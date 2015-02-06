def fib(n):
	fib1 = 1
	fib2 = 0
	for i in xrange(n - 1):
		temp = fib2
		fib2 = fib1
		fib1 += temp
	return fib1

def n_digit_fibonacci(n):
	i = 1
	while True:
		num = fib(i)
		if len(str(num)) == n:
			return i
		i += 1

print n_digit_fibonacci(1000)