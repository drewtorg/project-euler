import math

def is_curious(num):
	digits = list(str(num))
	sum = 0
	for digit in digits:
		sum += math.factorial(int(digit))
	if sum != num:
		return False
	return True

def sum_all_curious(limit):
	total = 0
	for i in xrange(3, limit):
		if is_curious(i):
			total += i
	return total

#1000000 should be enough to find ALL the curious numbers, right?
print sum_all_curious(1000000)