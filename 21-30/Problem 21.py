def is_amicable(a, b):
	if a == b:
		return False

	if sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a:
		return True

	return False

def sum_of_proper_divisors(num):
	sum = 0
	for x in xrange(1, num):
		if num % x == 0:
			sum += x
	return sum

def sum_of_amicable(limit):
	sum = 0
	for a in xrange(220, limit):
		for b in xrange(a + 1, limit):
			if is_amicable(a,b):
				sum += a + b
	return sum

print sum_of_amicable(10000)

#works but takes FOREVER
