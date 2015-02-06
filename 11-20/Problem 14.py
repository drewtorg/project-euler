def collatz_sequence(num):
	count = 0
	while num > 1:
		if num % 2 == 0:
			num /= 2
		else:
			num = 3*num + 1
		count += 1
	return count

def longest_collatz_sequence(num):
	maxVal = 0
	maxIndex = 0
	for n in xrange(num):
		temp = collatz_sequence(n)
		if maxVal <= temp:
			maxVal = temp;
			maxIndex = n
	return maxIndex

print longest_collatz_sequence(1000000)